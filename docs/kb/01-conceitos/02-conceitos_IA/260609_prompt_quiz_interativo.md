---
title: "PROMPT COMPLETO PARA O HORIZONS"
source: "https://docs.google.com/document/u/0/d/1WcabdPd6UPA9txoHj1E2YPPR1ZLV1B3YForx6g5HtlM/mobilebasic"
author:
published:
created: 2026-06-09
description: "PROMPT COMPLETO PARA O HORIZONS Quiz: \"Descubra o Maior Gargalo do Seu Instagram\" Cole este prompt diretamente no campo de texto do Horizons da Hostinger. Antes de usar, crie uma conta gratuita em emailjs.com e substitua os três valores indicados no prompt pelo seu Service ID, Template ID e Publi..."
tags:
  - "clippings"
---
## Quiz: "Descubra o Maior Gargalo do Seu Instagram"

Cole este prompt diretamente no campo de texto do Horizons da Hostinger. Antes de usar, crie uma conta gratuita em emailjs.com e substitua os três valores indicados no prompt pelo seu Service ID, Template ID e Public Key do EmailJS.

---

## PROMPT

Crie um web app completo de quiz de diagnóstico chamado "Descubra o Maior Gargalo do Seu Instagram". Este quiz será usado por profissionais de mídias sociais e donos de negócios para identificar o principal problema que está limitando os resultados do seu Instagram.

---

### DESIGN E IDENTIDADE VISUAL

Crie um design moderno, limpo e profissional com as seguintes especificações:

- Fundo geral: branco (#FFFFFF)
- Cor primária de destaque: laranja vibrante (#FF6600)
- Cor secundária: azul escuro (#051933)
- Fonte do título: bold, moderna, sem serifa
- Fonte do corpo: regular, legível, sem serifa
- O layout deve ser 100% responsivo e mobile-first, pensado para ser acessado pelo celular
- Cantos arredondados em todos os cards e botões (border-radius de 12px)
- Sombra suave nos cards (box-shadow leve)
- Animação de transição suave entre as telas (fade ou slide)
- Ícone de raio ou Instagram estilizado no topo da tela de boas-vindas

---

### ESTRUTURA GERAL DO APP

O app tem quatro telas distintas:

1. Tela de boas-vindas
2. Tela de captura de dados
3. Tela das perguntas
4. Tela de resultado

---

### TELA 1 — BOAS-VINDAS

Exiba:

- Ícone grande (raio ou gráfico de crescimento, em laranja)
- Título principal: "Descubra o Maior Gargalo do Seu Instagram"
- Subtítulo: "Responda 7 perguntas rápidas e receba um diagnóstico personalizado com o que está travando o crescimento do seu perfil."
- Lista visual com três bullets e ícones de check laranja:
- "Diagnóstico 100% gratuito"
- "Resultado em menos de 2 minutos"
- "Recomendações práticas e personalizadas"
- Botão laranja grande: "Quero meu diagnóstico"
- Ao clicar, vai para a Tela 2

---

### TELA 2 — CAPTURA DE DADOS

Exiba:

- Título: "Antes de começar, me conta quem você é"
- Subtítulo menor: "Vou usar essas informações para enviar o resultado completo do seu diagnóstico."
- Campo de texto: Nome (obrigatório, placeholder: "Seu nome")
- Campo de email: E-mail (obrigatório, placeholder: "Seu melhor e-mail")
- Campo de texto: WhatsApp (opcional, placeholder: "DDD + número — ex: 11999999999")
- Checkbox obrigatório com texto: "Concordo em receber o resultado do diagnóstico por e-mail"
- Botão laranja grande: "Começar o quiz"
- Texto menor abaixo do botão: "Seus dados são usados apenas para enviar o diagnóstico. Sem spam."
- Validação: nome e e-mail são obrigatórios. Se não preenchidos, exibir mensagem de erro em vermelho suave abaixo do campo.
- Ao clicar em "Começar o quiz" com campos válidos, vai para a Tela 3

---

### TELA 3 — PERGUNTAS

Regras de interface:

- Exibir uma pergunta por vez
- Barra de progresso no topo mostrando a porcentagem de avanço (ex: "Pergunta 3 de 7")
- A barra de progresso é laranja e cresce a cada pergunta respondida
- Cada opção de resposta é um card clicável com borda suave
- Ao selecionar uma opção, o card fica com fundo laranja claro e borda laranja, sem precisar clicar em "próxima"
- Botão "Próxima" aparece após a seleção, no canto inferior direito
- Na última pergunta, o botão muda para "Ver meu diagnóstico"
- Cada resposta tem um valor de pontuação de 1 a 4 (1 é o pior cenário, 4 é o melhor)

---

#### AS 7 PERGUNTAS

Pergunta 1 Título: "Com que frequência você publica no Instagram?" Opções (em ordem, com valores indicados entre colchetes para uso interno no cálculo):

- "Raramente, menos de uma vez por semana" \[1\]
- "Uma a duas vezes por semana" \[2\]
- "Três a quatro vezes por semana" \[3\]
- "Todo dia ou quase todos os dias" \[4\]

Pergunta 2 Título: "Você tem uma estratégia de conteúdo definida?" Opções:

- "Não tenho nada definido, posto quando lembro" \[1\]
- "Tenho uma ideia geral na cabeça, mas nada documentado" \[2\]
- "Tenho um calendário editorial que sigo" \[3\]
- "Tenho estratégia com objetivos, formatos e métricas definidas" \[4\]

Pergunta 3 Título: "Você analisa as métricas do seu perfil?" Opções:

- "Nunca analiso os números" \[1\]
- "Analiso de vez em quando, sem regularidade" \[2\]
- "Analiso uma vez por mês" \[3\]
- "Analiso semanalmente e ajusto a estratégia com base nos dados" \[4\]

Pergunta 4 Título: "Como você responde comentários e DMs?" Opções:

- "Respondo quando lembro, sem rotina definida" \[1\]
- "Respondo a maioria em até 24 horas" \[2\]
- "Respondo tudo em poucas horas" \[3\]
- "Tenho automação que responde na hora e organiza os atendimentos" \[4\]

Pergunta 5 Título: "Você usa chamadas para ação (CTAs) nos seus posts?" Opções:

- "Não costumo usar CTA" \[1\]
- "Coloco CTA em alguns posts" \[2\]
- "Sempre coloco CTA nos posts" \[3\]
- "Tenho CTA estratégico no perfil, nos posts e nos stories com destinos diferentes" \[4\]

Pergunta 6 Título: "Como está a qualidade visual do seu perfil hoje?" Subitem: "(foto, bio, destaques, identidade visual)" Opções:

- "Precisa melhorar bastante" \[1\]
- "Está razoável, mas falta profissionalismo" \[2\]
- "Está bom, mas poderia ser mais consistente" \[3\]
- "Está profissional, coerente e transmite credibilidade" \[4\]

Pergunta 7 Título: "O seu Instagram está gerando resultados para o seu negócio?" Opções:

- "Não estou tendo nenhum resultado visível" \[1\]
- "Tenho alguns resultados, mas abaixo do esperado" \[2\]
- "Estou tendo bons resultados, mas poderia ser melhor" \[3\]
- "Estou satisfeito com os resultados e quero escalar" \[4\]

---

### LÓGICA DE CÁLCULO DO DIAGNÓSTICO

Some os valores das 7 respostas. O total varia de 7 a 28. Com base na pontuação, exiba o diagnóstico correspondente:

7 a 12 pontos — Diagnóstico: "Invisível no Instagram"

13 a 17 pontos — Diagnóstico: "Ativo mas Sem Direção"

18 a 22 pontos — Diagnóstico: "Quase Lá"

23 a 28 pontos — Diagnóstico: "Pronto para Escalar"

---

### TELA 4 — RESULTADO

Layout da tela de resultado:

- Exibir no topo: "Olá, \[Nome\]! Seu diagnóstico está pronto."
- Badge colorido com o nome do diagnóstico (fundo laranja, texto branco, canto arredondado)
- Ícone correspondente ao diagnóstico (ver abaixo)
- Título grande com o nome do diagnóstico
- Subtítulo: "Veja o que está travando o seu crescimento e o que fazer agora"
- Bloco de texto com a descrição completa do diagnóstico (ver abaixo)
- Seção "Seus principais pontos de atenção" com até 3 bullets em laranja
- Seção "O que fazer agora" com 3 ações recomendadas numeradas
- Linha divisória
- Botão laranja grande: "Falar com um especialista" que abre wa.me/5512991919482 em nova aba. Substitua \[NÚMERO\_WHATSAPP\] pelo número do profissional no formato internacional sem símbolos, ex: 5511999999999
- Botão secundário (outline laranja): "Compartilhar meu resultado" que gera um texto para compartilhamento e abre o app de compartilhamento nativo do celular
- Mensagem final: "O resultado completo foi enviado para \[e-mail informado\]. Verifique sua caixa de entrada."

---

### CONTEÚDO DOS 4 DIAGNÓSTICOS

---

DIAGNÓSTICO 1: "Invisível no Instagram" Ícone: fantasma ou sinal de wifi cortado Pontuação: 7 a 12

Descrição: "Seu Instagram ainda não está trabalhando por você. A combinação de baixa frequência, falta de estratégia e pouco engajamento faz com que o algoritmo praticamente ignore o seu perfil, o que significa que mesmo as pessoas que te seguem raramente veem o seu conteúdo."

Pontos de atenção:

- Consistência é o primeiro passo: sem frequência mínima, o algoritmo pune o perfil
- Sem estratégia, você posta sem propósito e não sabe o que está funcionando
- Seu perfil pode não estar passando a credibilidade que o negócio merece

O que fazer agora:

1. Defina uma frequência realista e cumpra por 30 dias seguidos, mesmo que comece com 3 posts por semana
2. Escolha dois formatos de conteúdo para testar (Reels e carrossel são os que mais entregam alcance em 2026) e foque neles
3. Revise seu perfil: foto, bio e destaques precisam comunicar quem você é e o que você oferece nos primeiros 3 segundos

---

DIAGNÓSTICO 2: "Ativo mas Sem Direção" Ícone: bússola sem norte ou seta circulando Pontuação: 13 a 17

Descrição: "Você está publicando, mas sem uma estratégia clara que conecte o conteúdo ao seu objetivo de negócio. Isso gera bastante trabalho sem retorno proporcional. O algoritmo percebe que você está ativo, mas o seu público ainda não entende com clareza o que você oferece e por que deveria te contratar."

Pontos de atenção:

- Quantidade sem estratégia não converte, cria apenas movimento sem direção
- Sem análise de métricas, você não sabe o que está funcionando e continua repetindo o que não traz resultado
- CTAs ausentes ou fracos fazem o lead interessado não saber qual é o próximo passo

O que fazer agora:

1. Defina um objetivo claro para o Instagram: geração de leads, vendas diretas ou autoridade. Tudo que você posta deve servir a esse objetivo
2. Comece a olhar os números uma vez por semana: alcance, salvamentos e compartilhamentos são os três sinais que mais indicam o que vale continuar fazendo
3. Coloque um CTA diferente em cada post e teste qual gera mais resposta do seu público

---

DIAGNÓSTICO 3: "Quase Lá" Ícone: alvo com flecha próxima do centro Pontuação: 18 a 22

Descrição: "Você já tem uma base sólida: posta com consistência, tem noção de estratégia e está engajando com a audiência. O problema é que ainda falta afinar os detalhes que fazem a diferença entre um perfil que cresce e um que converte de verdade. Você está investindo tempo e energia, mas o retorno ainda não está proporcional ao esforço."

Pontos de atenção:

- O crescimento está acontecendo, mas a conversão em clientes pode melhorar com pequenos ajustes de funil
- Você provavelmente não está aproveitando todo o potencial das automações disponíveis para Instagram
- A diferença entre o seu resultado atual e o próximo nível pode estar em um único ajuste de posicionamento ou formato

O que fazer agora:

1. Revise o funil completo: do post até o fechamento. Onde as pessoas param de avançar? No link da bio? No DM? Na proposta?
2. Implemente pelo menos uma automação de entrega de conteúdo ou atendimento para liberar o seu tempo das tarefas operacionais
3. Teste um formato de conteúdo que você ainda não explorou e meça por 30 dias

---

DIAGNÓSTICO 4: "Pronto para Escalar" Ícone: foguete ou gráfico subindo Pontuação: 23 a 28

Descrição: "Parabéns. Você está entre os profissionais mais preparados estrategicamente no Instagram. Tem consistência, estratégia, análise de dados e engajamento ativo. Agora o seu desafio é escalar o que já funciona sem aumentar proporcionalmente o tempo que você investe."

Pontos de atenção:

- No seu estágio, o próximo salto vem de sistemas, não de mais esforço
- Automações inteligentes podem multiplicar o alcance do que você já faz bem
- Você está em posição de oferecer isso como diferencial competitivo para os seus clientes

O que fazer agora:

1. Mapeie quais tarefas do seu Instagram ainda são manuais e que poderiam ser automatizadas sem perder a autenticidade
2. Considere criar uma isca digital interativa para capturar leads qualificados diretamente dos seus posts
3. Estruture um processo de onboarding para novos clientes que inclua a configuração de pelo menos uma automação de atendimento

---

### ENVIO DE EMAIL COM O RESULTADO — USANDO EMAILJS

Após o usuário ver o resultado, disparar automaticamente um e-mail usando o serviço EmailJS.

Instruções de implementação: Inclua no HTML o script do EmailJS: <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>

Use os seguintes parâmetros de chamada:

emailjs.init("SUA\_PUBLIC\_KEY"); // substitua pela sua Public Key do EmailJS

emailjs.send("SEU\_SERVICE\_ID", "SEU\_TEMPLATE\_ID", {

to\_name: nomeUsuario,

to\_email: emailUsuario,

whatsapp: whatsappUsuario,

diagnostico\_nome: nomeDiagnostico,

diagnostico\_descricao: descricaoDiagnostico,

pontos\_atencao: pontosAtencao,

acoes: acoesSugeridas,

pontuacao\_total: pontuacaoTotal,

data: new Date().toLocaleDateString('pt-BR')

});

O template do e-mail no EmailJS deve conter:

- Assunto: "Seu diagnóstico do Instagram está aqui, {{to\_name}}"
- Corpo: resultado completo formatado com o nome do diagnóstico, descrição, pontos de atenção e ações recomendadas
- Assinatura do profissional responsável

Nota no código: adicione um comentário explicando que o usuário precisa criar conta gratuita em emailjs.com, criar um serviço de e-mail, criar um template e substituir os três valores acima pelos seus próprios.

---

### INTEGRAÇÃO COM WHATSAPP

Quando o campo de WhatsApp for preenchido na Tela 2, ao exibir o resultado crie dinamicamente um link wa.me com mensagem pré-preenchida:

Formato do link: https://wa.me/55\[NUMERO\_SEM\_ESPACOS\]?text=Olá!%20Acabei%20de%20fazer%20o%20diagnóstico%20do%20Instagram%20e%20meu%20resultado%20foi:%20\[NOME\_DIAGNOSTICO\].%20Gostaria%20de%20conversar%20sobre%20como%20melhorar%20meu%20perfil.

Este link deve aparecer como botão secundário "Receber resultado pelo WhatsApp" na tela de resultado, abrindo em nova aba.

---

### BOTÃO DE COMPARTILHAMENTO

O botão "Compartilhar meu resultado" deve usar a Web Share API nativa do navegador com o seguinte conteúdo:

navigator.share({

title: 'Meu diagnóstico do Instagram',

text: \`Fiz o diagnóstico gratuito do Instagram e descobri que sou: "${nomeDiagnostico}". Quer saber qual é o seu maior gargalo? Faz o quiz também!\`,

url: window.location.href

});

Se o navegador não suportar a Web Share API, mostrar um campo de texto com o conteúdo para copiar manualmente.

---

### DETALHES TÉCNICOS FINAIS

- Todo o app deve funcionar em um único arquivo HTML com CSS e JavaScript embutidos, sem dependências externas além do script do EmailJS
- Use localStorage para salvar temporariamente os dados do usuário durante a sessão, sem enviar para nenhum servidor externo além do EmailJS
- Nenhuma informação deve ser enviada a terceiros exceto o e-mail via EmailJS
- O app deve funcionar offline após o primeiro carregamento, exceto o envio de e-mail
- Adicione no topo do código um bloco de comentário com instruções claras de configuração: onde substituir a Public Key, Service ID e Template ID do EmailJS, e onde colocar o número de WhatsApp do profissional
- O app não deve ter nenhum botão de voltar entre as perguntas para garantir que o usuário complete o quiz sem pular questões
- O resultado deve ser exibido imediatamente após a última pergunta, sem tela de carregamento longa

ENDOFFILE echo "Arquivo criado com sucesso"