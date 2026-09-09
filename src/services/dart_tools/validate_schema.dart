import 'dart:convert';
import 'dart:io';

import 'package:http/http.dart' as http;

const supabaseUrl = 'https://drezioycqhgsmpcqwskw.supabase.co';
const serviceRoleKey =
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRyZXppb3ljcWhnc21wY3F3c2t3Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MzA1MDU0MCwiZXhwIjoyMDc4NjI2NTQwfQ.cErdcIs99ApkYDfOlE3AOOT73ugbWHW7J_dZ51Nxtj4';

class SupabaseSchemaClient {
  final String url;
  final String apiKey;

  SupabaseSchemaClient({required this.url, required this.apiKey});

  Future<List<Map<String, dynamic>>> fetchSupabaseBasic() async {
    final response = await http.get(
      Uri.parse('$url/rest/v1/data_models_supabase_basic'),
      headers: {
        'apikey': apiKey,
        'Authorization': 'Bearer $apiKey',
        'Content-Type': 'application/json',
        'Accept-Profile': 'flutter_config',
      },
    );

    if (response.statusCode != 200) {
      throw Exception(
          'Erro ao buscar data_models_supabase_basic: ${response.statusCode} - ${response.body}');
    }

    return List<Map<String, dynamic>>.from(jsonDecode(response.body));
  }

  Future<List<Map<String, dynamic>>> fetchFlutterStatic() async {
    final response = await http.get(
      Uri.parse('$url/rest/v1/data_models_flutter_static'),
      headers: {
        'apikey': apiKey,
        'Authorization': 'Bearer $apiKey',
        'Content-Type': 'application/json',
        'Accept-Profile': 'flutter_config',
      },
    );

    if (response.statusCode != 200) {
      throw Exception(
          'Erro ao buscar data_models_flutter_static: ${response.statusCode} - ${response.body}');
    }

    return List<Map<String, dynamic>>.from(jsonDecode(response.body));
  }

  Future<List<Map<String, dynamic>>> fetchFlutterDynamic() async {
    final response = await http.get(
      Uri.parse('$url/rest/v1/data_models_flutter_dynamic'),
      headers: {
        'apikey': apiKey,
        'Authorization': 'Bearer $apiKey',
        'Content-Type': 'application/json',
        'Accept-Profile': 'flutter_config',
      },
    );

    if (response.statusCode != 200) {
      throw Exception(
          'Erro ao buscar data_models_flutter_dynamic: ${response.statusCode} - ${response.body}');
    }

    return List<Map<String, dynamic>>.from(jsonDecode(response.body));
  }

  Future<List<Map<String, dynamic>>> fetchDataModelsSupabase() async {
    final response = await http.get(
      Uri.parse('$url/rest/v1/data_models_supabase'),
      headers: {
        'apikey': apiKey,
        'Authorization': 'Bearer $apiKey',
        'Content-Type': 'application/json',
        'Accept-Profile': 'flutter_config',
      },
    );

    if (response.statusCode != 200) {
      throw Exception(
          'Erro ao buscar data_models_supabase: ${response.statusCode} - ${response.body}');
    }

    return List<Map<String, dynamic>>.from(jsonDecode(response.body));
  }
}

List<String> validateSchema({
  required List<Map<String, dynamic>> supabaseBasic,
  required List<Map<String, dynamic>> flutterStatic,
  required List<Map<String, dynamic>> flutterDynamic,
  required List<Map<String, dynamic>> dataModelsSupabase,
}) {
  final errors = <String>[];

  // Cria conjunto de colunas por schema/tabela a partir de supabase_basic (fonte da verdade)
  // Chave: "schema.table"
  final supabaseByTable = <String, Set<String>>{};
  for (final row in supabaseBasic) {
    final tableSchema = row['tbl_table_schema'] as String? ?? 'public';
    final tableName = row['tbl_table_name'] as String? ?? '';
    final columnName = row['col_column_name'] as String?;
    if (tableName.isEmpty || columnName == null || columnName.isEmpty) continue;

    final key = '$tableSchema.$tableName';
    supabaseByTable.putIfAbsent(key, () => {});
    supabaseByTable[key]!.add(columnName);
  }

  // Cria conjunto de colunas por schema/tabela a partir de flutter_static
  final flutterStaticByTable = <String, Set<String>>{};
  for (final row in flutterStatic) {
    final tableSchema = row['tbl_table_schema'] as String? ?? 'public';
    final tableName = row['tbl_table_name'] as String? ?? '';
    final columnName = row['col_column_name'] as String?;
    if (tableName.isEmpty || columnName == null || columnName.isEmpty) continue;

    final key = '$tableSchema.$tableName';
    flutterStaticByTable.putIfAbsent(key, () => {});
    flutterStaticByTable[key]!.add(columnName);
  }

  // Cria conjunto de colunas por schema/tabela a partir de flutter_dynamic
  final flutterDynamicByTable = <String, Set<String>>{};
  for (final row in flutterDynamic) {
    final tableSchema = row['tbl_table_schema'] as String? ?? 'public';
    final tableName = row['tbl_table_name'] as String? ?? '';
    final columnName = row['col_column_name'] as String?;
    if (tableName.isEmpty || columnName == null || columnName.isEmpty) continue;

    final key = '$tableSchema.$tableName';
    flutterDynamicByTable.putIfAbsent(key, () => {});
    flutterDynamicByTable[key]!.add(columnName);
  }

  // Cria conjunto de colunas por schema/tabela a partir de data_models_supabase (VIEW)
  final supabaseViewByTable = <String, Set<String>>{};
  for (final row in dataModelsSupabase) {
    final tableSchema = row['tbl_table_schema'] as String? ?? 'public';
    final tableName = row['tbl_table_name'] as String? ?? '';
    final columnName = row['col_column_name'] as String?;
    if (tableName.isEmpty || columnName == null || columnName.isEmpty) continue;

    final key = '$tableSchema.$tableName';
    supabaseViewByTable.putIfAbsent(key, () => {});
    supabaseViewByTable[key]!.add(columnName);
  }

  // Verifica se flutter_static está de acordo com supabase_basic
  for (final tableKey in supabaseByTable.keys) {
    final supabaseCols = supabaseByTable[tableKey]!;
    final staticCols = flutterStaticByTable[tableKey] ?? {};
    final dynamicCols = flutterDynamicByTable[tableKey] ?? {};
    final viewCols = supabaseViewByTable[tableKey] ?? {};

    // Colunas em supabase_basic que faltam em flutter_static
    for (final col in supabaseCols.difference(staticCols)) {
      errors.add('$tableKey.$col: falta em flutter_static');
    }

    // Colunas em flutter_static que não existem em supabase_basic
    for (final col in staticCols.difference(supabaseCols)) {
      errors.add('$tableKey.$col: sobra em flutter_static (não existe em supabase_basic)');
    }

    // Colunas em supabase_basic que faltam em flutter_dynamic
    for (final col in supabaseCols.difference(dynamicCols)) {
      errors.add('$tableKey.$col: falta em flutter_dynamic');
    }

    // Colunas em flutter_dynamic que não existem em supabase_basic
    for (final col in dynamicCols.difference(supabaseCols)) {
      errors.add('$tableKey.$col: sobra em flutter_dynamic (não existe em supabase_basic)');
    }

    // Colunas em supabase_basic que faltam na VIEW data_models_supabase
    for (final col in supabaseCols.difference(viewCols)) {
      errors.add('$tableKey.$col: falta em data_models_supabase (VIEW)');
    }

    // Colunas na VIEW que não existem em supabase_basic
    for (final col in viewCols.difference(supabaseCols)) {
      errors.add('$tableKey.$col: sobra em data_models_supabase (VIEW)');
    }
  }

  // Verifica tabelas em flutter_static/dynamic que não existem em supabase_basic
  for (final tableKey in flutterStaticByTable.keys) {
    if (!supabaseByTable.containsKey(tableKey)) {
      errors.add('$tableKey: existe em flutter_static mas não em supabase_basic');
    }
  }

  for (final tableKey in flutterDynamicByTable.keys) {
    if (!supabaseByTable.containsKey(tableKey)) {
      errors.add('$tableKey: existe em flutter_dynamic mas não em supabase_basic');
    }
  }

  // Verifica tabelas na VIEW que não existem em supabase_basic
  for (final tableKey in supabaseViewByTable.keys) {
    if (!supabaseByTable.containsKey(tableKey)) {
      errors.add('$tableKey: existe em data_models_supabase (VIEW) mas não em supabase_basic');
    }
  }

  // Imprime resumo por tabela (apenas nome da tabela para simplificar)
  final tables = supabaseByTable.keys.toList()..sort();
  print('=== Tabelas encontradas: ${tables.length} ===\n');
  for (final tableKey in tables) {
    final staticCols = flutterStaticByTable[tableKey]?.length ?? 0;
    final dynamicCols = flutterDynamicByTable[tableKey]?.length ?? 0;
    final viewCols = supabaseViewByTable[tableKey]?.length ?? 0;
    final total = supabaseByTable[tableKey]!.length;
    print('$tableKey: $staticCols static, $dynamicCols dynamic, $viewCols view ($total total em supabase_basic)');
  }
  print('');

  return errors;
}

Future<void> main() async {
  print('=== Validando Schema do Flutter ===\n');

  final client = SupabaseSchemaClient(url: supabaseUrl, apiKey: serviceRoleKey);

  print('1. Buscando dados do Supabase...');
  final supabaseBasic = await client.fetchSupabaseBasic();
  final flutterStatic = await client.fetchFlutterStatic();
  final flutterDynamic = await client.fetchFlutterDynamic();
  final dataModelsSupabase = await client.fetchDataModelsSupabase();
  print('   ✓ data_models_supabase_basic: ${supabaseBasic.length} registros');
  print('   ✓ data_models_flutter_static: ${flutterStatic.length} registros');
  print('   ✓ data_models_flutter_dynamic: ${flutterDynamic.length} registros');
  print('   ✓ data_models_supabase (VIEW): ${dataModelsSupabase.length} registros\n');

  print('2. Validando schema (supabase_basic = fonte da verdade)...');
  final errors = validateSchema(
    supabaseBasic: supabaseBasic,
    flutterStatic: flutterStatic,
    flutterDynamic: flutterDynamic,
    dataModelsSupabase: dataModelsSupabase,
  );

  print('=== Resumo ===');
  print('Erros: ${errors.length}');

  if (errors.isEmpty) {
    print('\n✓ Schema válido!');
  } else {
    print('\n✗ Existem erros a corrigir:');
    for (final error in errors) {
      print('  - $error');
    }
    exit(1);
  }
}
