import 'dart:convert';
import 'package:http/http.dart' as http;

const supabaseUrl = 'https://drezioycqhgsmpcqwskw.supabase.co';
const serviceRoleKey =
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImRyZXppb3ljcWhnc21wY3F3c2t3Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MzA1MDU0MCwiZXhwIjoyMDc4NjI2NTQwfQ.cErdcIs99ApkYDfOlE3AOOT73ugbWHW7J_dZ51Nxtj4';

void main() async {
  print('=== Schemas Expostos pela API ===\n');

  final response = await http.get(
    Uri.parse('$supabaseUrl/rest/v1/'),
    headers: {
      'apikey': serviceRoleKey,
      'Authorization': 'Bearer $serviceRoleKey',
      'Accept': 'application/json',
    },
  );

  if (response.statusCode == 200) {
    final data = jsonDecode(response.body) as Map;
    final paths = data['paths'] as Map;
    
    final schemas = <String>{};
    
    for (final path in paths.keys) {
      // Paths começam com /nome_tabela ou /schema/nome_tabela
      final parts = path.toString().split('/');
      if (parts.length >= 2) {
        // Se tem 2 partes, é só tabela (schema = public)
        // Se tem 3 partes, é schema.tabela
        if (parts.length == 2) {
          schemas.add('public');
        } else if (parts.length > 2) {
          // Verificar se é uma tabela (não é o path raiz)
          if (parts[1].isNotEmpty && !parts[1].startsWith('{')) {
            schemas.add(parts[1]);
          }
        }
      }
    }

    print('Schemas expostos pela API:\n');
    final sortedSchemas = schemas.toList()..sort();
    for (final schema in sortedSchemas) {
      print('- $schema');
    }
    print('\nTotal: ${sortedSchemas.length} schema(s)');
  } else {
    print('Erro: ${response.statusCode} - ${response.body}');
  }
}
