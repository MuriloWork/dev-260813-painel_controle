# Model: 260913-termboard_model_repository_v03

## Overview
Repository concept model v03 - Aligned to SKOS/RDFS/OWL.
Uses `skos:narrower` for hierarchy and qualified subproperties of `skos:related` with `rdfs:domain`/`rdfs:range` constraints.

## Namespace Prefixes
```
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix repo: <https://termboard.com/ontology/e8f9a0b1-c2d3-4e5f-6a7b-8c9d0e1f2a3b#> .
```

## Property Hierarchy
```
skos:related (SKOS base)
├── repo:contains         (domain: Repository/Branch | range: Commit)
├── repo:produces         (domain: Repository | range: Release)
├── repo:uses             (domain: Repository | range: Tag)
├── repo:managedBy        (domain: Repository | range: VersionControlTool)
├── repo:supports         (domain: Repository | range: Branch)
├── repo:hasRemote        (domain: Repository | range: Remote)
├── repo:stores           (domain: Repository | range: Merge)
├── repo:allowsCloneOf    (domain: Repository | range: Clone)
├── repo:receivesPullRequest (domain: Repository | range: PullRequest)
├── repo:undergoes        (domain: Branch | range: Merge)
├── repo:references       (domain: PullRequest | range: Branch)
├── repo:isMarkedBy       (domain: Release | range: Tag)
├── repo:sourceOf         (domain: Remote | range: Clone)
└── repo:containsBranches (domain: Remote | range: Branch)

skos:narrower (SKOS hierarchy)
├── code repository       (domain: CodeRepository | range: Repository)
├── artifact repository   (domain: ArtifactRepository | range: Repository)
├── data repository       (domain: DataRepository | range: Repository)
└── documentation repository (domain: DocumentationRepository | range: Repository)
```

## Concepts

### Top Concept
- **repository** (skos:Concept, skos:topConceptOf Repository Scheme)

### Narrower Concepts (Types)
- code repository → skos:narrower → repository
- artifact repository → skos:narrower → repository
- data repository → skos:narrower → repository
- documentation repository → skos:narrower → repository

### Related Concepts (Entities)
- branch, tag, release, remote, commit, merge, clone, pull request, version control tool

## Terms
# name | description | type | weight
repository | A centralized, version-controlled storage system for managing digital assets. | concept | 2
code repository | A specialized repository for storing and versioning source code. | term | 1
artifact repository | A repository for storing build artifacts, libraries, and binaries. | term | 1
data repository | A repository for storing structured or unstructured data assets. | term | 1
documentation repository | A repository for managing project documentation and knowledge base. | term | 1
branch | A parallel line of development within a repository. | term | 1
tag | A named pointer to a specific commit, used to mark releases. | term | 1
release | A packaged version of the software at a specific point in time. | term | 1
remote | A version of a repository hosted on a server. | term | 1
commit | A single snapshot of the repository state at a point in time. | term | 1
merge | The process of combining changes from one branch into another. | term | 1
clone | The action of creating a local copy of a remote repository. | term | 1
pull request | A proposal to merge changes from one branch into another. | term | 1
version control tool | Software that tracks changes to files (e.g., Git, SVN). | term | 1

## Relations
# source | relationName | target | id | description | additionalInformation
code repository | skos:narrower | repository | r001-... | Hierarchical: code repository is narrower | Domain: CodeRepository | Range: Repository
artifact repository | skos:narrower | repository | r002-... | Hierarchical: artifact repository is narrower | Domain: ArtifactRepository | Range: Repository
data repository | skos:narrower | repository | r003-... | Hierarchical: data repository is narrower | Domain: DataRepository | Range: Repository
documentation repository | skos:narrower | repository | r004-... | Hierarchical: documentation repository is narrower | Domain: DocumentationRepository | Range: Repository
repository | repo:supports | branch | r005-... | Repository supports branch | Domain: Repository | Range: Branch
repository | repo:uses | tag | r006-... | Repository uses tags | Domain: Repository | Range: Tag
repository | repo:produces | release | r007-... | Repository produces releases | Domain: Repository | Range: Release
repository | repo:hasRemote | remote | r008-... | Repository has remote | Domain: Repository | Range: Remote
repository | repo:contains | commit | r009-... | Repository contains commits | Domain: Repository | Range: Commit
repository | repo:stores | merge | r010-... | Repository stores merges | Domain: Repository | Range: Merge
repository | repo:allowsCloneOf | clone | r011-... | Repository allows cloning | Domain: Repository | Range: Clone
repository | repo:receivesPullRequest | pull request | r012-... | Repository receives PRs | Domain: Repository | Range: PullRequest
repository | repo:managedBy | version control tool | r013-... | Repository managed by VCS | Domain: Repository | Range: VersionControlTool
branch | repo:undergoes | merge | r014-... | Branch undergoes merge | Domain: Branch | Range: Merge
branch | repo:contains | commit | r015-... | Branch contains commits | Domain: Branch | Range: Commit
pull request | repo:references | branch | r016-... | PR references branch | Domain: PullRequest | Range: Branch
release | repo:isMarkedBy | tag | r017-... | Release marked by tag | Domain: Release | Range: Tag
remote | repo:sourceOf | clone | r018-... | Remote is source of clone | Domain: Remote | Range: Clone
remote | repo:containsBranches | branch | r019-... | Remote contains branches | Domain: Remote | Range: Branch

## Changes from v02

1. **Qualified Properties** - All `skos:related` replaced with specific subproperties
2. **Domain/Range** - Each property has formal `rdfs:domain` and `rdfs:range`
3. **Property Hierarchy** - Clear hierarchy: `repo:X rdfs:subPropertyOf skos:related`
4. **OWL ObjectProperty** - All properties defined as `owl:ObjectProperty`
5. **Inference Support** - Any `repo:X` is automatically also `skos:related`
