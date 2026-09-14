# Model: 260912-termboard_model_repository

# === MODEL GUIDANCE ===
# Use EXACT matching for names and IDs when updating existing elements.
# Use '-' as a placeholder for fields that are not applicable to a specific type.
# Use pipe (|) as column separator.
# Do not change the header comments (lines starting with #).
# TYPE GUIDE:
# - Term (term): A concept, entity, or element in the domain
# - Concept (concept): An abstract idea or notion
# - Property (property): An attribute or characteristic of a term
# - Group (group): A visual container for grouping related terms
# - Connection Point (conpoint): A junction point for complex relations

## Terms
# name | description | type | weight
repository | A repository is a centralized, version-controlled storage system for managing and tracking changes to source code or other digital assets over time. | concept | 1
code repository | A specialized repository dedicated to storing and versioning source code, often supporting features like branching and merge management. | term | 1
artifact repository | A centralized repository for storing build artifacts, libraries, and binaries, commonly used in continuous integration and deployment pipelines. | term | 1
data repository | A repository designed to store structured or unstructured data assets, such as datasets, schemas, or configuration files, with version control. | term | 1
documentation repository | A repository specifically for managing and versioning project documentation, guides, and knowledge base entries. | term | 1
version control system | Software that tracks changes to files and allows users to manage different versions of the data, forming the core mechanism of a repository. | term | 1
commit | A single snapshot of the state of the repository at a specific point in time, representing a discrete change or update. | term | 1
branch | A parallel line of development within a repository that allows for independent work without affecting the main codebase until merged. | term | 1
merge | The process of combining changes from one branch into another, integrating development work into the repository's main history. | term | 1
pull request | A mechanism for proposing changes to a repository, allowing for review and discussion before the changes are officially merged. | term | 1

## Relations
# source | relationName | target | id | description | additionalInformation | cardinality | cardinalitySource
documentation repository | is-a | repository | 4073b8e2-7031-0881-8921-4e7c1d1b8af2 |  |  |  | 
code repository | is-a | repository | 374d4a0f-547b-79e8-e8de-e74fd30958ff |  |  |  | 
artifact repository | is-a | repository | 075bb5eb-5ca2-8fd6-be7b-6a780de9e77f |  |  |  | 
data repository | is-a | repository | 931fa919-194a-c73e-68df-71fcf2973cbe |  |  |  | 
repository | contains | commit | fce0acd1-1294-4a97-e442-e96d81db7538 |  |  |  | 

