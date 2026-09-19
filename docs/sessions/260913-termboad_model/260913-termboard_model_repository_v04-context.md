# 1. Model: 260913-termboard_model_repository_v04

## 1.1. Overview
Repository concept model v04 - **Faceted Classification**.
Repository is a hub concept linked to multiple independent facets (Content, Structure, Process, Tool, Scope).
Supports polyhierarchy and mixin classes.

## 1.2. Design Pattern: Faceted Classification

Instead of creating fixed subclasses (`code repo`, `doc repo`), we separate **characteristics** into independent groups. A single repository can have multiple facets simultaneously.

```
                    ┌─────────────────────┐
                    │     repository      │  ← Hub concept
                    │   (skos:Concept)    │
                    └──────────┬──────────┘
                               │
       ┌───────────┬───────────┼───────────┬───────────┐
       │           │           │           │           │
  ┌────▼────┐ ┌────▼────┐ ┌────▼────┐ ┌────▼────┐ ┌────▼────┐
  │ CONTENT │ │STRUCTURE│ │ PROCESS │ │  TOOL   │ │  SCOPE  │
  │ (facet) │ │ (facet) │ │ (facet) │ │ (facet) │ │ (facet) │
  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘
       │           │           │           │           │
  ┌────┴────┐ ┌────┴────┐ ┌────┴────┐ ┌────┴────┐ ┌────┴────┐
  │code     │ │folder   │ │commit   │ │git      │ │local    │
  │document │ │file     │ │merge    │ │svn      │ │remote   │
  │data     │ │branch   │ │release  │ │mercurial│ │private  │
  │artifact │ │tag      │ │clone    │ │         │ │public   │
  │config   │ │symlink  │ │PR       │ │         │ │         │
  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘
```

## 1.3. Namespace Prefixes

```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix repo: <https://termboard.com/ontology/f1a2b3c4-d5e6-7890-abcd-ef1234567890#> .
```

## 1.4. ConceptSchemes (Facets)

| Facet | ConceptScheme | Purpose |
|-------|---------------|---------|
| **Content** | repo:ContentScheme | What the repository stores |
| **Structure** | repo:StructureScheme | How it's organized |
| **Process** | repo:ProcessScheme | What operations happen |
| **Tool** | repo:ToolScheme | What manages it |
| **Scope** | repo:ScopeScheme | Access and visibility |

## 1.5. Concepts by Facet

### 1.5.1. Content (What is stored)
| Concept | Label | Synonyms |
|---------|-------|----------|
| repo:CodeContent | code content | source code, programming files |
| repo:DocumentContent | document content | documentation, knowledge base |
| repo:DataContent | data content | datasets, configuration |
| repo:ArtifactContent | artifact content | binaries, packages |
| repo:ConfigContent | config content | configuration files, IaC |

### 1.5.2. Structure (How it's organized)
| Concept | Label | Synonyms |
|---------|-------|----------|
| repo:Folder | folder | directory, path |
| repo:File | file | source file, artifact file |
| repo:Branch | branch | feature branch, dev branch |
| repo:Tag | tag | version tag, release tag |

### 1.5.3. Process (What happens)
| Concept | Label | Synonyms |
|---------|-------|----------|
| repo:Commit | commit | revision, changeset |
| repo:Merge | merge | integration, branch merge |
| repo:Release | release | version, build |
| repo:Clone | clone | checkout, local copy |
| repo:PullRequest | pull request | merge request, code review |

### 1.5.4. Tool (What manages it)
| Concept | Label | Synonyms |
|---------|-------|----------|
| repo:Git | Git | git |
| repo:SVN | SVN | Subversion, Apache Subversion |
| repo:Mercurial | Mercurial | Hg |

### 1.5.5. Scope (Access/Visibility)
| Concept | Label | Synonyms |
|---------|-------|----------|
| repo:Local | local | local only |
| repo:Remote | remote | hosted, server |
| repo:Private | private | restricted, internal access |
| repo:Public | public | open, open source |

## 1.6. Linking Properties (Repository ↔ Facets)

| Property | Domain | Range | SubpropertyOf |
|----------|--------|-------|---------------|
| repo:hasContent | Repository | ContentFacet | skos:related |
| repo:hasStructure | Repository | StructureFacet | skos:related |
| repo:hasProcess | Repository | ProcessFacet | skos:related |
| repo:hasTool | Repository | ToolFacet | skos:related |
| repo:hasScope | Repository | ScopeFacet | skos:related |

## 1.7. Internal Relations (Within Facets)

### 1.7.1. Structure Relations
| Property | Domain | Range |
|----------|--------|-------|
| repo:hasFile | Folder | File |
| repo:hasBranch | Repository | Branch |
| repo:hasTag | Branch | Tag |

### 1.7.2. Process Relations
| Property | Domain | Range |
|----------|--------|-------|
| repo:produces | Process | Release |
| repo:markedBy | Release | Tag |
| repo:undergoes | Branch | Merge |
| repo:references | PullRequest | Branch |
| repo:sourceOf | Remote | Clone |

### 1.7.3. Cross-Facet Relations
| Property | Domain | Range |
|----------|--------|-------|
| repo:contains | Structure | Content |
| repo:organizedBy | Content | Structure |

## 1.8. Example: Multi-Faceted Repository

```turtle
# A repository that is BOTH code AND documentation
repo:meu-projeto a repo:Repository ;
    skos:prefLabel "meu-projeto" ;
    # Content facets
    repo:hasContent repo:CodeContent, repo:DocumentContent ;
    # Structure facets
    repo:hasStructure repo:Folder, repo:File, repo:Branch ;
    # Process facets
    repo:hasProcess repo:Commit, repo:Merge, repo:Tag ;
    # Tool facets
    repo:hasTool repo:Git ;
    # Scope facets
    repo:hasScope repo:Private, repo:Remote .
```

## 1.9. Inference Support

Any `repo:hasX` property is also `skos:related` (via `rdfs:subPropertyOf`).
This means:
- All facet links are automatically recognized by SKOS tools
- The hub-and-spoke model is compatible with existing SKOS infrastructure
- Polyhierarchy is supported without multiple inheritance conflicts

## 1.10. Changes from v03

1. **Faceted Classification** - Repository is a hub, not a hierarchy root
2. **Independent ConceptSchemes** - Each facet is a separate scheme
3. **Linking Properties** - `repo:hasContent`, `repo:hasStructure`, etc.
4. **No Fixed Subclasses** - Repository type is determined by its facets
5. **Polyhierarchy Support** - Repository can have multiple content types simultaneously
6. **Cross-Facet Relations** - Structure contains Content, Process produces Release, etc.
