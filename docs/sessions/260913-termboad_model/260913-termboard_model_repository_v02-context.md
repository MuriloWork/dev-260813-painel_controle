# Model: 260913-termboard_model_repository_v02

## Overview
Repositório de conhecimento sobre repositories - Modelo v02 alinhado ao SKOS (Simple Knowledge Organization System).

## SKOS Alignment
This model uses SKOS standard relations:
- `skos:broader` / `skos:narrower` - Hierarchical taxonomy
- `skos:related` - Associative (non-hierarchical) relations

## Concept Structure

### Top Concept
- **repository** (Concept) - Top-level concept in the Repository Concept Scheme

### Narrower Concepts (Types of Repository)
- **code repository** → skos:narrower → repository
- **artifact repository** → skos:narrower → repository
- **data repository** → skos:narrower → repository
- **documentation repository** → skos:narrower → repository

### Related Concepts (Associations)
- **branch** - skos:related → repository
- **tag** - skos:related → repository
- **release** - skos:related → repository
- **remote** - skos:related → repository
- **commit** - skos:related → repository
- **merge** - skos:related → repository
- **clone** - skos:related → repository
- **pull request** - skos:related → repository
- **version control tool** - skos:related → repository

## Terms
# name | description | type | weight
repository | A centralized, version-controlled storage system for managing and tracking changes to digital assets over time. | concept | 2
code repository | A specialized repository dedicated to storing and versioning source code, often supporting features like branching and merge management. | term | 1
artifact repository | A centralized repository for storing build artifacts, libraries, and binaries, commonly used in CI/CD pipelines. | term | 1
data repository | A repository designed to store structured or unstructured data assets, such as datasets, schemas, or configuration files. | term | 1
documentation repository | A repository specifically for managing and versioning project documentation, guides, and knowledge base entries. | term | 1
branch | A parallel line of development within a repository that allows for independent work without affecting the main codebase until merged. | term | 1
tag | A named pointer to a specific commit, used to mark releases, versions, or important milestones. | term | 1
release | A packaged version of the software at a specific point in time, typically tagged and ready for deployment. | term | 1
remote | A version of a repository hosted on a server (e.g., GitHub, GitLab), allowing collaboration. | term | 1
commit | A single snapshot of the state of the repository at a specific point in time. | term | 1
merge | The process of combining changes from one branch into another. | term | 1
clone | The action of creating a local copy of a remote repository. | term | 1
pull request | A proposal to merge changes from one branch into another, enabling code review. | term | 1
version control tool | Software that tracks changes to files and allows users to manage different versions (e.g., Git, SVN). | term | 1

## Relations
# source | relationName | target | id | description | additionalInformation | cardinality | cardinalitySource
code repository | skos:narrower | repository | r001-... | Hierarchical: code repository is a narrower concept of repository | SKOS: skos:narrower - taxonomy |  | 
artifact repository | skos:narrower | repository | r002-... | Hierarchical: artifact repository is a narrower concept of repository | SKOS: skos:narrower - taxonomy |  | 
data repository | skos:narrower | repository | r003-... | Hierarchical: data repository is a narrower concept of repository | SKOS: skos:narrower - taxonomy |  | 
documentation repository | skos:narrower | repository | r004-... | Hierarchical: documentation repository is a narrower concept of repository | SKOS: skos:narrower - taxonomy |  | 
repository | skos:related | branch | r005-... | Associative: repository supports branch | SKOS: skos:related - associative |  | 
repository | skos:related | tag | r006-... | Associative: repository uses tags | SKOS: skos:related - associative |  | 
repository | skos:related | release | r007-... | Associative: repository produces releases | SKOS: skos:related - associative |  | 
repository | skos:related | remote | r008-... | Associative: repository can have a remote counterpart | SKOS: skos:related - associative |  | 
repository | skos:related | commit | r009-... | Associative: repository contains commits | SKOS: skos:related - associative |  | 
repository | skos:related | merge | r010-... | Associative: repository stores merge operations | SKOS: skos:related - associative |  | 
repository | skos:related | clone | r011-... | Associative: repository can be cloned | SKOS: skos:related - associative |  | 
repository | skos:related | pull request | r012-... | Associative: pull request proposes changes to repository | SKOS: skos:related - associative |  | 
repository | skos:related | version control tool | r013-... | Associative: repository is managed by a version control tool | SKOS: skos:related - associative |  | 
branch | skos:related | merge | r014-... | Associative: branch undergoes merge | SKOS: skos:related - associative |  | 
branch | skos:related | commit | r015-... | Associative: branch contains commits | SKOS: skos:related - associative |  | 
pull request | skos:related | branch | r016-... | Associative: pull request references a branch | SKOS: skos:related - associative |  | 
release | skos:related | tag | r017-... | Associative: release is marked by a tag | SKOS: skos:related - associative |  | 
remote | skos:related | clone | r018-... | Associative: remote is the source of clone | SKOS: skos:related - associative |  | 
remote | skos:related | branch | r019-... | Associative: remote contains branches | SKOS: skos:related - associative |  | 

## Changes from v01

1. **ConceptScheme Added** - Repository is now the top concept in a formal scheme
2. **SKOS Relations** - All relations now use SKOS standard (broader/narrower/related)
3. **New Concepts Added** - tag, release, remote, clone
4. **Event/Process Separation** - commit, merge, clone are now clearly identified as processes/events
5. **Tool Separation** - version control tool is now a separate concept (not a type of repository)
6. **Synonyms Expanded** - Each term has relevant synonyms for better discoverability
