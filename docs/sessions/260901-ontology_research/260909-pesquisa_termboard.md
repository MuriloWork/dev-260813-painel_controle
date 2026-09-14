# 1. Avaliação do TermBoard para iniciantes

Sim, **é uma boa porta de entrada**. Li o manual completo em `termboard.com/manual/`. Veredito:

**Bom para:** fase conceitual, aprender a diferença `Conceito x Propriedade x Relação`, fazer workshop com especialistas, gerar a primeira versão OWL/SKOS sem instalar nada.

**Não substitui:** Protégé + reasoner quando o modelo amadurecer.

## 1.1. Prós

* **Roda 100% no browser, sem login.** Privacidade total, ideal para testar: `termboard.com` > `GET STARTED`.
* **Conceitos alinhados à modelagem semântica:** `Term` (genérico) / `Concept` (entidade, o "substantivo") / `Property` (atributo, o "adjetivo"). É exatamente a distinção que o guia [Semantic Model](https://termboard.com/manual/howto/semantic-model.html) ensina.
* **Tipos de relação + cardinalidade:** `Generalization` (is-a), `Composition`, `Aggregation`, `Interaction`, etc. + `1`, `0..1`, `1..*`. Isso já te ensina a pensar em OWL.
* **Model Checks:** pega duplicata, hierarquia circular, termo isolado, sem descrição, relação bidirecional redundante. Em `Right sidebar > Model Checks`.
* **Import/Export OWL e SKOS de verdade:** `File > Import/Export > OWL Ontology`
  * Import: `.owl/.rdf/.xml`, `.ttl`, `.jsonld` padrão. Mapeia `owl:Class -> Concept`, `owl:ObjectProperty -> Relation`, `rdfs:subClassOf -> Generalization`, `owl:DatatypeProperty -> XField`.
  * Export: `RDF/XML`, `Turtle`, `JSON-LD` padrão, com opção `Vocabulary Style: OWL / SKOS / Both`. Round-trip com Protégé funciona.
  * SKOS: `skos:Concept`, `skos:broader/narrower/related`, `skos:prefLabel/altLabel/definition`. Ver em [Import/Export](https://termboard.com/manual/page/import-export.html#skos-vocabularies).
* **Guias how-to excelentes:** [Semantic Model](https://termboard.com/manual/howto/semantic-model.html) com workshop de 10 passos e [Knowledge Graph](https://termboard.com/manual/howto/knowledge-graph.html) com exemplo Biblioteca `termboard.com/app?demo=library`.
* **IA + TermStorm:** `Tools > Bulk Add/Chatbot > "Knowledge Graph about a subject"` gera rascunho. Bom para destravar, mas valide com especialista.

## 1.2. Contras / pegadinhas para iniciante

1.  **Não tem template OWL/SKOS pronto.** Em `File > New from Template` só tem: `User Story Map`, `Conceptual Data Model`, `Mind Map`, `Process Flow`. O mais próximo é `Conceptual Data Model`. Você vai começar do blank e configurar.
2.  **JSON-LD duplo:** existe `Export JSON-LD (Termboard Format)` proprietário/experimental e `Export OWL > JSON-LD` padrão. Para `owl/json-ld` use sempre o segundo. Não importe JSON-LD externo via `Import JSON-LD`, use `Import OWL Ontology`.
3.  **Simplifica OWL complexo:** property chains, restrições complexas são simplificadas. Limite prático de ~2000 classes.
4.  **Sem reasoner:** os checks são estruturais, não lógicos como HermiT no Protégé.
5.  **Save no browser se perde:** salve sempre `File > Save File > JSON`.

> Nota 7.5/10 para iniciantes. Melhor fluxo: modela visual no TermBoard > exporta `Turtle` > valida no Protégé.

# 2. Instruções + template

## 2.1. OWL ou SKOS?

* **OWL:** ontologia formal, classes + `ObjectProperty` + domínio/range + cardinalidade. Use para Knowledge Graph com inferência.
* **SKOS:** vocabulário controlado/taxonomia/tesauro. Use para listas, tags, categorias. Só `Concept`, `broader/narrower/related`, `prefLabel/altLabel`.
* No TermBoard na exportação você escolhe `Both` e ganha os dois.

## 2.2. Passo a passo no TermBoard

1.  **Escopo:** defina 1 frase de domínio. Ex: "Acervo de biblioteca".
2.  **Novo:** `File > New from Template > Conceptual Data Model` ou canvas em branco.
3.  **Crie 10-15 Conceitos:** `SHIFT+Click` ou `Bulk Add`. Marque `Type = concept`. Nomes no singular: `Livro`, `Autor`, não `Livros`.
4.  **Hierarquia:** crie `Relation Type = Generalization`. Ex: `Romance -> Ficção -> Gênero`. Isso vira `rdfs:subClassOf` / `skos:broader`.
5.  **Relações:** verbo direcional. `Livro -escrito por-> Autor`, `Filial -possui-> Livro`. Defina cardinalidade na `Relation sidebar`.
6.  **Propriedades:** crie `Type = property`: `ISBN`, `Título`. Ligue `Livro -has property-> ISBN`.
7.  **Documente tudo:** `description` vira `rdfs:comment / skos:definition`. Sinônimo vira `skos:altLabel`.
8.  **Valide:** `Model Checks` + `Hierarchy view` + `Find path`.
9.  **Exporte:** `File > Export > OWL Ontology`, `Base URI: https://example.org/biblioteca#`, `Format: Turtle (.ttl)` - melhor para git - e `Vocabulary Style: Both`, marque `descriptions + synonyms + cardinality`.
10. **Round-trip:** abra o `.ttl` no Protégé para validar.

## 2.3. Template pronto para importar

`File > Import > JSON`, cole isso:

```json
{
  "metadata": {
    "id": "biblioteca-modelo",
    "name": "Modelo Biblioteca - Inicial",
    "author": "Você",
    "description": "Template inicial OWL/SKOS: conceitos, hierarquia, relações e propriedades"
  },
  "terms": [
    { "id": "C1", "name": "Livro", "type": "concept", "description": "Obra publicada catalogada no acervo" },
    { "id": "C2", "name": "Autor", "type": "concept", "description": "Pessoa que escreve uma obra" },
    { "id": "C3", "name": "Editora", "type": "concept", "description": "Organização que publica a obra" },
    { "id": "C4", "name": "Gênero", "type": "concept", "description": "Categoria literária" },
    { "id": "C5", "name": "Ficção", "type": "concept", "description": "Gênero de obra imaginativa" },
    { "id": "C6", "name": "Filial", "type": "concept", "description": "Unidade física da biblioteca" },
    { "id": "P1", "name": "ISBN", "type": "property", "description": "Identificador único do livro" },
    { "id": "P2", "name": "Título", "type": "property", "description": "Título principal da obra" }
  ],
  "relations": [
    { "source": "C5", "target": "C4", "name": "is subclass of", "relationType": "Generalization" },
    { "source": "C1", "target": "C2", "name": "escrito por", "relationType": "Association", "cardinality": "1..*" },
    { "source": "C1", "target": "C3", "name": "publicado por", "relationType": "Association", "cardinality": "1" },
    { "source": "C1", "target": "C4", "name": "pertence a", "relationType": "Association" },
    { "source": "C6", "target": "C1", "name": "possui", "relationType": "Association", "cardinality": "0..*" },
    { "source": "C1", "target": "P1", "name": "has property", "relationType": "Association" },
    { "source": "C1", "target": "P2", "name": "has property", "relationType": "Association" }
  ]
}
```

Esse JSON gera no export OWL, em `Turtle`:

```turtle
@prefix : <https://example.org/biblioteca#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

:Livro a owl:Class, skos:Concept ;
  rdfs:label "Livro"@pt ;
  rdfs:comment "Obra publicada catalogada no acervo"@pt ;
  skos:prefLabel "Livro"@pt .

:Ficcao a owl:Class, skos:Concept ;
  rdfs:subClassOf :Genero ;
  skos:broader :Genero ;
  rdfs:label "Ficção"@pt .

:escritoPor a owl:ObjectProperty ;
  rdfs:label "escrito por"@pt ;
  rdfs:domain :Livro ;
  rdfs:range :Autor .
```

Você não precisa escrever isso à mão - o TermBoard gera. O exemplo acima é para entender o que sai.

Para praticar importação, teste também: `File > Import > OWL Ontology` com FOAF de `TEST/foaf-simple.rdf` e `File > Load Examples > FIBO`.

Qual é o seu domínio real? Se me disser ex: "painel de controle", "financeiro", "produtos", eu adapto esse template com seus 10-15 conceitos iniciais já em JSON importável + `Turtle` base.


