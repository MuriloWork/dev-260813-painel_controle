import 'dart:convert';
import 'dart:io';
import 'package:analyzer/dart/analysis/analysis_context_collection.dart';
import 'package:analyzer/dart/analysis/results.dart';
import 'package:analyzer/dart/ast/ast.dart';
import 'package:analyzer/dart/ast/visitor.dart'; // Corrected import
import 'package:analyzer/source/line_info.dart'; // Corrected import
import 'package:path/path.dart' as path;
import 'package:analyzer/dart/ast/token.dart'; // Import Token
import 'package:analyzer/dart/element/element.dart'; // Add this import
import 'package:analyzer/file_system/physical_file_system.dart'; // New Import


// AstCounterVisitor (from original)
class AstCounterVisitor extends RecursiveAstVisitor<void> {
  int classDeclarationCount = 0;
  bool foundTargetClass = false;
  final String targetClassName;

  AstCounterVisitor(this.targetClassName);

  @override
  void visitClassDeclaration(ClassDeclaration node) {
    classDeclarationCount++;
    if (node.name.lexeme == targetClassName) {
      foundTargetClass = true;
    }
    super.visitClassDeclaration(node); // Continue traversal
  }
}

// AstToJsonVisitor para gerar JSON da AST (renamed from DebugAstToJsonVisitor)
class AstToJsonVisitor extends RecursiveAstVisitor<void> {
  final LineInfo _lineInfo;
  Map<String, dynamic>? _root;
  final List<Map<String, dynamic>> _stack = [];

  final ResolvedUnitResult _resolvedResult; // Use ResolvedUnitResult instead of AnalysisSession
  AstToJsonVisitor(this._lineInfo, this._resolvedResult);

  Map<String, dynamic>? get jsonOutput => _root;

  Map<String, dynamic> _createJsonNodeBase(AstNode node) {
    final Map<String, dynamic> jsonNode = {};
    jsonNode['type'] = node.runtimeType.toString();
    jsonNode['offset'] = node.offset;
    jsonNode['length'] = node.length;
    jsonNode['line'] = _lineInfo.getLocation(node.offset).lineNumber;
    jsonNode['column'] = _lineInfo.getLocation(node.offset).columnNumber;
    jsonNode['source_text'] = node.toSource(); // Adiciona o texto fonte do nó

    // Helper function to get name from Identifier/Token
    String? _getName(dynamic node) {
      if (node == null) return null;
      if (node is Identifier) {
        return node.name; // Identifier has .name
      } else if (node is Token) {
        return node.lexeme; // Token has .lexeme
      }
      return node.toString(); // Fallback for any other unexpected type
    }

    // Add staticType for Expression nodes
    if (node is Expression) {
      jsonNode['staticType'] =
          node.staticType?.getDisplayString(withNullability: true);
    }

    // Add name for declaration nodes
    if (node is ClassDeclaration) {
      jsonNode['name'] = node.name.lexeme;
    } else if (node is MethodDeclaration) {
      jsonNode['name'] = node.name.lexeme;
    } else if (node is FunctionDeclaration) {
      jsonNode['name'] = node.name.lexeme;
    } else if (node is FieldDeclaration) {
      // Field declarations can have multiple variables, typically the first is the primary name
      if (node.fields.variables.isNotEmpty) {
        jsonNode['name'] = node.fields.variables.first.name.lexeme;
      }
    } else if (node is VariableDeclaration) {
      jsonNode['name'] = node.name.lexeme;
    } else if (node is MethodInvocation) {
      jsonNode['methodName'] = _getName(node.methodName);
    } else if (node is BinaryExpression) {
      jsonNode['operator'] = node.operator.lexeme;
    } else if (node is AssignmentExpression) {
      jsonNode['operator'] = node.operator.lexeme;
    } else if (node is InstanceCreationExpression) {
      String? constructorName;
      final constructorIdentifier = node.constructorName.name; // SimpleIdentifier?
      final typeIdentifier = node.constructorName.type.name; // Identifier or Token

      if (constructorIdentifier != null) {
        // Named constructor (e.g., SomeClass.namedConstructor)
        constructorName = _getName(constructorIdentifier);
      } else {
        // Unnamed constructor (e.g., SomeClass())
        constructorName = _getName(typeIdentifier);
      }
      
      if (constructorName != null && constructorName.isNotEmpty) {
        jsonNode['constructorName'] = constructorName;
      }
    } else if (node is PropertyAccess) {
      jsonNode['propertyName'] = _getName(node.propertyName);
    }


    // Add literals and identifiers
    if (node is SimpleStringLiteral) {
      jsonNode['value'] = node.value;
    } else if (node is IntegerLiteral) {
      jsonNode['value'] = node.value;
    } else if (node is BooleanLiteral) {
      jsonNode['value'] = node.value;
    } else if (node is SimpleIdentifier) {
      jsonNode['value'] = node.name;
    } else if (node is PrefixedIdentifier) {
      jsonNode['value'] = node.name;
    }
    return jsonNode;
  }

  void _addNode(AstNode node, [Map<String, dynamic>? additionalData]) {
    final jsonNode = _createJsonNodeBase(node);
    if (additionalData != null) {
      jsonNode.addAll(additionalData); // Add any additional data
    }
    if (_root == null) {
      _root = jsonNode;
    }
    if (_stack.isNotEmpty) {
      // Adiciona o nó atual como filho do nó no topo da pilha
      (_stack.last['children'] ??= []).add(jsonNode);
    }
    _stack.add(jsonNode);
  }

  void _popNode() {
    _stack.removeLast();
  }

  @override
  void visitCompilationUnit(CompilationUnit node) {
    _addNode(node);
    super.visitCompilationUnit(node);
    _popNode();
  }

  @override
  void visitClassDeclaration(ClassDeclaration node) {
    _addNode(node);
    super.visitClassDeclaration(node);
    _popNode();
  }

  @override
  void visitMethodDeclaration(MethodDeclaration node) {
    final Map<String, dynamic> additionalData = {};
    if (node.returnType != null) { // This line is expected to cause a compile-time error.
      additionalData['returnType'] = node.returnType!.toSource();
    }
    _addNode(node, additionalData);
    super.visitMethodDeclaration(node);
    _popNode();
  }

  @override
  void visitFunctionDeclaration(FunctionDeclaration node) {
    final Map<String, dynamic> additionalData = {};
    if (node.returnType != null) {
      additionalData['returnType'] = node.returnType!.toSource();
    }
    _addNode(node, additionalData);
    super.visitFunctionDeclaration(node);
    _popNode();
  }

  @override
  void visitFieldDeclaration(FieldDeclaration node) {
    _addNode(node);
    super.visitFieldDeclaration(node);
    _popNode();
  }

  @override
  void visitVariableDeclaration(VariableDeclaration node) {
    _addNode(node);
    super.visitVariableDeclaration(node);
    _popNode();
  }

  @override
  void visitSimpleIdentifier(SimpleIdentifier node) {
    _addNode(node);
    super.visitSimpleIdentifier(node);
    _popNode();
  }

  // Common concrete types that typically exist in RecursiveAstVisitor
  @override
  void visitReturnStatement(ReturnStatement node) {
    _addNode(node);
    super.visitReturnStatement(node);
    _popNode();
  }

  @override
  void visitMethodInvocation(MethodInvocation node) {
    _addNode(node);
    super.visitMethodInvocation(node);
    _popNode();
  }

  @override
  void visitBinaryExpression(BinaryExpression node) {
    _addNode(node);
    super.visitBinaryExpression(node);
    _popNode();
  }

  @override
  void visitAssignmentExpression(AssignmentExpression node) {
    _addNode(node);
    super.visitAssignmentExpression(node);
    _popNode();
  }
  
  @override
  void visitExpressionStatement(ExpressionStatement node) {
    _addNode(node);
    super.visitExpressionStatement(node);
    _popNode();
  }

  @override
  void visitBlock(Block node) {
    _addNode(node);
    super.visitBlock(node);
    _popNode();
  }
  
  @override
  void visitIfStatement(IfStatement node) {
    _addNode(node);
    super.visitIfStatement(node);
    _popNode();
  }

  @override
  void visitBlockFunctionBody(BlockFunctionBody node) {
    _addNode(node);
    super.visitBlockFunctionBody(node);
    _popNode();
  }
  
  @override
  void visitNamedExpression(NamedExpression node) {
    _addNode(node);
    super.visitNamedExpression(node);
    _popNode();
  }
  
  @override
  void visitSimpleStringLiteral(SimpleStringLiteral node) {
    _addNode(node);
    super.visitSimpleStringLiteral(node);
    _popNode();
  }

  @override
  void visitIntegerLiteral(IntegerLiteral node) {
    _addNode(node);
    super.visitIntegerLiteral(node);
    _popNode();
  }

  @override
  void visitBooleanLiteral(BooleanLiteral node) {
    _addNode(node);
    super.visitBooleanLiteral(node);
    _popNode();
  }

  @override
  void visitPropertyAccess(PropertyAccess node) {
    _addNode(node);
    super.visitPropertyAccess(node);
    _popNode();
  }

  @override
  void visitInstanceCreationExpression(InstanceCreationExpression node) {
    _addNode(node);
    super.visitInstanceCreationExpression(node);
    _popNode();
  }

  @override
  void visitArgumentList(ArgumentList node) {
    _addNode(node);
    super.visitArgumentList(node);
    _popNode();
  }

  @override
  void visitFormalParameterList(FormalParameterList node) {
    _addNode(node);
    super.visitFormalParameterList(node);
    _popNode();
  }

  @override
  void visitSimpleFormalParameter(SimpleFormalParameter node) {
    _addNode(node);
    super.visitSimpleFormalParameter(node);
    _popNode();
  }

  @override
  void visitTypeArgumentList(TypeArgumentList node) {
    _addNode(node);
    super.visitTypeArgumentList(node);
    _popNode();
  }

  @override
  void visitTypeParameterList(TypeParameterList node) {
    _addNode(node);
    super.visitTypeParameterList(node);
    _popNode();
  }

  @override
  void visitTypeParameter(TypeParameter node) {
    _addNode(node);
    super.visitTypeParameter(node);
    _popNode();
  }
  
  @override
  void visitPrefixedIdentifier(PrefixedIdentifier node) {
    _addNode(node);
    super.visitPrefixedIdentifier(node);
    _popNode();
  }

  @override
  void visitFunctionExpression(FunctionExpression node) {
    _addNode(node);
    super.visitFunctionExpression(node);
    _popNode();
  }

  @override
  void visitParenthesizedExpression(ParenthesizedExpression node) {
    _addNode(node);
    super.visitParenthesizedExpression(node);
    _popNode();
  }
  
  @override
  void visitFieldFormalParameter(FieldFormalParameter node) {
    _addNode(node);
    super.visitFieldFormalParameter(node);
    _popNode();
  }

  @override
  void visitConstructorDeclaration(ConstructorDeclaration node) {
    _addNode(node);
    super.visitConstructorDeclaration(node);
    _popNode();
  }

  @override
  void visitConstructorName(ConstructorName node) {
    _addNode(node);
    super.visitConstructorName(node);
    _popNode();
  }

  @override
  void visitConditionalExpression(ConditionalExpression node) {
    _addNode(node);
    super.visitConditionalExpression(node);
    _popNode();
  }
  
  @override
  void visitIndexExpression(IndexExpression node) {
    _addNode(node);
    super.visitIndexExpression(node);
    _popNode();
  }

  @override
  void visitAsExpression(AsExpression node) {
    _addNode(node);
    super.visitAsExpression(node);
    _popNode();
  }

  @override
  void visitIsExpression(IsExpression node) {
    _addNode(node);
    super.visitIsExpression(node);
    _popNode();
  }

  @override
  void visitNullLiteral(NullLiteral node) {
    _addNode(node);
    super.visitNullLiteral(node);
    _popNode();
  }
  
  @override
  void visitListLiteral(ListLiteral node) {
    _addNode(node);
    super.visitListLiteral(node);
    _popNode();
  }

  @override
  void visitMapLiteralEntry(MapLiteralEntry node) {
    _addNode(node);
    super.visitMapLiteralEntry(node);
    _popNode();
  }
  
  @override
  void visitSetOrMapLiteral(SetOrMapLiteral node) {
    _addNode(node);
    super.visitSetOrMapLiteral(node);
    _popNode();
  }
  
  @override
  void visitSpreadElement(SpreadElement node) {
    _addNode(node);
    super.visitSpreadElement(node);
    _popNode();
  }

  @override
  void visitCascadeExpression(CascadeExpression node) {
    _addNode(node);
    super.visitCascadeExpression(node);
    _popNode();
  }

  @override
  void visitFunctionDeclarationStatement(FunctionDeclarationStatement node) {
    _addNode(node);
    super.visitFunctionDeclarationStatement(node);
    _popNode();
  }

  @override
  void visitSwitchStatement(SwitchStatement node) {
    _addNode(node);
    super.visitSwitchStatement(node);
    _popNode();
  }

  @override
  void visitSwitchCase(SwitchCase node) {
    _addNode(node);
    super.visitSwitchCase(node);
    _popNode();
  }

  @override
  void visitSwitchDefault(SwitchDefault node) {
    _addNode(node);
    super.visitSwitchDefault(node);
    _popNode();
  }

  @override
  void visitDoStatement(DoStatement node) {
    _addNode(node);
    super.visitDoStatement(node);
    _popNode();
  }

  @override
  void visitWhileStatement(WhileStatement node) {
    _addNode(node);
    super.visitWhileStatement(node);
    _popNode();
  }

  @override
  void visitForStatement(ForStatement node) {
    _addNode(node);
    super.visitForStatement(node);
    _popNode();
  }

  @override
  void visitBreakStatement(BreakStatement node) {
    _addNode(node);
    super.visitBreakStatement(node);
    _popNode();
  }

  @override
  void visitContinueStatement(ContinueStatement node) {
    _addNode(node);
    super.visitContinueStatement(node);
    _popNode();
  }

  @override
  void visitEmptyStatement(EmptyStatement node) {
    _addNode(node);
    super.visitEmptyStatement(node);
    _popNode();
  }

  @override
  void visitAssertStatement(AssertStatement node) {
    _addNode(node);
    super.visitAssertStatement(node);
    _popNode();
  }

  @override
  void visitTopLevelVariableDeclaration(TopLevelVariableDeclaration node) {
    _addNode(node);
    super.visitTopLevelVariableDeclaration(node);
    _popNode();
  }

  @override
  void visitImportDirective(ImportDirective node) {
    _addNode(node);
    super.visitImportDirective(node);
    _popNode();
  }

  @override
  void visitExportDirective(ExportDirective node) {
    _addNode(node);
    super.visitExportDirective(node);
    _popNode();
  }

  @override
  void visitPartDirective(PartDirective node) {
    _addNode(node);
    super.visitPartDirective(node);
    _popNode();
  }

  @override
  void visitPartOfDirective(PartOfDirective node) {
    _addNode(node);
    super.visitPartOfDirective(node);
    _popNode();
  }

  @override
  void visitConstructorFieldInitializer(ConstructorFieldInitializer node) {
    _addNode(node);
    super.visitConstructorFieldInitializer(node);
    _popNode();
  }

  @override
  void visitSuperConstructorInvocation(SuperConstructorInvocation node) {
    _addNode(node);
    super.visitSuperConstructorInvocation(node);
    _popNode();
  }

  @override
  void visitRedirectingConstructorInvocation(RedirectingConstructorInvocation node) {
    _addNode(node);
    super.visitRedirectingConstructorInvocation(node);
    _popNode();
  }

  @override
  void visitFunctionTypeAlias(FunctionTypeAlias node) {
    _addNode(node);
    super.visitFunctionTypeAlias(node);
    _popNode();
  }

  @override
  void visitGenericFunctionType(GenericFunctionType node) {
    final Map<String, dynamic> additionalData = {};
    if (node.returnType != null) {
      additionalData['returnType'] = node.returnType!.toSource();
    }
    _addNode(node, additionalData);
    super.visitGenericFunctionType(node);
    _popNode();
  }

  @override
  void visitComment(Comment node) {
    _addNode(node);
    super.visitComment(node);
    _popNode();
  }
}


// --- Função Principal de Análise Resolvida ---

Future<void> generateAst(String filePath, String projectRootPath, String? dartSdkPath) async {
  final file = File(filePath);
  if (!file.existsSync()) {
    print("Error: File not found at $filePath");
    exit(1);
  }
  
  try {
    // Explicitly set dartSdkPath
    final String explicitDartSdkPath = r'C:\Users\muril\flutter\bin\cache\dart-sdk'; // Use raw string for backslashes

    // 1. Cria a Coleção de Contexto de Análise
    final collection = AnalysisContextCollection(
      includedPaths: [projectRootPath],
      excludedPaths: [],
      sdkPath: explicitDartSdkPath, // Use the explicit SDK path
      resourceProvider: PhysicalResourceProvider.INSTANCE, // New: Add resourceProvider
    );

    final context = collection.contexts.first;
    final session = context.currentSession;

    // 2. Obtém a AST RESOLVIDA (ResolvedUnitResult)
    final resolvedResult = await session.getResolvedUnit(filePath);

    if (resolvedResult is ResolvedUnitResult) {
      if (resolvedResult.errors.isNotEmpty) {
        stderr.writeln(
            "⚠️ Warnings/Errors durante a análise (pode afetar a resolução semântica):");
        for (final error in resolvedResult.errors) {
          stderr.writeln(
              "- ${error.message} (${error.errorCode.name}) em linha ${resolvedResult.lineInfo.getLocation(error.offset).lineNumber}");
        }
      }


            final visitor = AstToJsonVisitor(resolvedResult.lineInfo, resolvedResult);
      resolvedResult.unit.accept(visitor); // Use accept to populate jsonOutput

      if (visitor.jsonOutput != null) {
        print(const JsonEncoder.withIndent('  ').convert(visitor.jsonOutput));
      } else {
        print("Could not generate AST JSON.");
      }

    } else {
      print('❌ Erro: Não foi possível obter o AST Resolvida para $filePath.');
      exit(1);
    }
  } catch (e) {
    print("Error processing $filePath: $e"); // Corrected string interpolation
    exit(1);
  }
}

void main(List<String> arguments) async {
  if (arguments.length < 2) {
    print('Usage: dart generate_resolved_ast.dart <file_path> <project_root_path>');
    exit(1);
  }

  // Resolve filePath to an absolute path
  final absoluteFilePath = path.normalize(path.join(Directory.current.path, arguments[0]));
  final projectRootPath = arguments[1];
  final dartSdkPath = arguments.length > 2 ? arguments[2] : null;

  await generateAst(absoluteFilePath, projectRootPath, dartSdkPath);
}
