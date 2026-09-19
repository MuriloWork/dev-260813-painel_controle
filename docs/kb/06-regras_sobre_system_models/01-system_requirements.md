# 1. Template para systems requirements

Para SysML, o núcleo de um requisito não é uma ficha com muitos campos. O elemento `requirement` possui fundamentalmente **identificador e texto**, e o valor do modelo vem principalmente das relações desse requisito com outros elementos: derivação, satisfação, verificação, refinamento e rastreamento. ([SysML.org](https://sysml.org/docs/specs/OMGSysML-FAS-06-05-04.pdf?utm_source=chatgpt.com "OMG SysML Specification"))

A própria SysML define o _Requirements Diagram_ como mecanismo para representar hierarquia/derivação de requisitos e relacioná-los aos elementos que os satisfazem e verificam. ([OMG](https://www.omg.org/sysml/sysmlv1/?utm_source=chatgpt.com "SysML® v1 Specification | Object Management Group"))

| Campo            | Papel                                                    |
| ---------------- | -------------------------------------------------------- |
| **ID**           | Identificação única                                      |
| **Requirement**  | Declaração do comportamento/condição requerida           |
| **Type**         | Tipo do requisito, quando necessário                     |
| **Source**       | Origem/necessidade que fundamenta o requisito            |
| **Derived from** | Requisito de nível superior, quando aplicável            |
| **Satisfies**    | Função ou elemento arquitetural que satisfaz o requisito |
| **Verified by**  | Método/caso de verificação                               |
| **Rationale**    | Justificativa, quando necessária                         |

A diferença importante é que **Source, Derived from, Satisfies e Verified by não devem ser tratados simplesmente como texto dentro do requisito**. Eles representam **relações do modelo**.

Isso é especialmente importante para o seu KMS porque permite construir a cadeia:

**necessidade → requisito → função → arquitetura → verificação**

O SEBoK enfatiza exatamente essa preocupação com rastreabilidade, incluindo origem/pai do requisito e critérios de sucesso de verificação como atributos úteis. ([SEBoK](https://sebokwiki.org/wiki/System_Requirements_Definition?utm_source=chatgpt.com "System Requirements Definition - SEBoK"))

Para a redação do requisito, a referência mais diretamente aplicável é a **INCOSE Guide to Writing Requirements**, que trata das características de declarações e conjuntos de requisitos e é explicitamente alinhada ao Systems Engineering Handbook e ao Needs and Requirements Manual. ([INCOSE Portal](https://portal.incose.org/Web/iCore/Store/StoreLayouts/Item_Detail.aspx?Category=EBOOKS&iProductCode=GUIDEWRITEREQ&utm_source=chatgpt.com "Guide to Writing Requirements (Soft Copy)"))

O caminho MBSE mais consistente é:

**necessidade → funções → requisitos funcionais → relações de rastreabilidade → arquitetura**  ([INCOSE](https://www.incose.org/docs/default-source/texas-gulf-coast/ieee_conference-2014-mbse-without-a-process-based-data-architecture-final-version.pdf?sfvrsn=42b8b9c6_0&utm_source=chatgpt.com "MBSE without a Process-Based Data Architecture"))

