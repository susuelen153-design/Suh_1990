"""Fonte única do repasse InHire: gera tarefas.json (quadro) e asana_import.csv (importação no Asana)."""
import csv, json, pathlib

HERE = pathlib.Path(__file__).parent
ATUAL = "Suellen Pereira da Silva"
SUC = ""  # sucessor(a) a definir no quadro

PLANILHA = "https://docs.google.com/spreadsheets/d/18XiwQr1AXpgs___fAk0nZDhYA5YvfpuokPxGPwHCTSE/edit"
FOTOS = "https://drive.google.com/drive/folders/1LdBZK69yVizn_WxvufqKtcIZsw4NvMR-"
MANUAL = "https://drive.google.com/file/d/19x416s7mUmxWs2ARTMga5m1RzBaG8huX/view"
INDICACAO = "https://drive.google.com/file/d/1p92SYhUJW0iSi7IKYZc9DwLgAq4t2YPp/view"
CIA = "https://www.ciadeestagios.com.br/"
GUPY = "https://docs.google.com/spreadsheets/d/1P8T1nctioHdNWqfhKaIlwD-fsDWVgiOgNpdBD180BF8/edit"

DELTA_T = "Programa Delta"
INHIRE_T = "InHire · Nova ATS"
TIPOS = {"p0":"Gestão do repasse","p12":"Manutenção",
         "p1":INHIRE_T,"p3":INHIRE_T,"p2":INHIRE_T,"p4":INHIRE_T,"p5":INHIRE_T,
         "p6":DELTA_T,"p7":DELTA_T,"p8":DELTA_T,"p9":DELTA_T,"p10":DELTA_T,"p11":DELTA_T}

# Situação no repasse, na ordem das tarefas: A=Atualizar (existe, precisa revisar), M=Manter (repassa como está), C=Criar (não existe), V=A avaliar
SITUACAO = "CCCCC" + "AAAAAAAAAAAAAC" + "MACAC" + "ACCC" + "ACCVC" + "CCCAMC" + "AAVCCCC" + "ACCCMC" + "CCCCVCC" + "CCCCC" + "CCCCCCCC" + "CCCA" + "CCC" + "C"
SIT = {"A":"Atualizar","M":"Manter","C":"Criar","V":"A avaliar"}

projects = [
    ("p0", "Transição e governança do repasse", "Organizar quem assume o quê, acessos e comunicação da saída."),
    ("p1", "Etapa 1 · Base final preenchida (importação)", "Planilha de Importação v4 com a InHire (Diego Guedes): LOTE 1 vagas abertas/congeladas, LOTE 2 fechadas/canceladas e talentos contratados."),
    ("p2", "Etapa 3 · Página de carreiras", "Página da Daycoval no InHire, com fotos do RH (set/26), textos e links das vagas."),
    ("p3", "Etapa 2 · Cartas proposta", "Modelos de carta proposta no InHire por tipo de contratação, com campos dinâmicos e aprovação."),
    ("p4", "Etapa 4 · Material de treinamento", "Treinamentos para lideranças, time de R&S e Programa de Indicação."),
    ("p5", "Etapa 5 · Documentação InHire", "Guia de processos, governança, SLAs e contatos para manter a operação sem a dona atual."),
    ("p6", "Delta · Estratégia, orçamento e aprovação", "Programa Delta (estágio de jovens talentos, 11 vagas em 7 áreas). Validação do KV, orçamento, fornecedor e cronograma."),
    ("p7", "Delta · Universidades e contatos", "Universidades target, cursos e canais (centro de carreiras, empresa júnior, ligas). Contatos ficam na aba Universidades."),
    ("p8", "Delta · Palestras e ativações", "Palestras, portas abertas, feiras e mailing para ativar 100–130 candidatos."),
    ("p9", "Delta · Marca e divulgação", "KV, hotsite, materiais e mídia com a Cia de Estágios e o Marketing."),
    ("p10", "Delta · Seleção e Challenge Day", "Testes, entrevistas, live de preparação, Challenge Day e entrevistas finais."),
    ("p12", "Bases mensais", "Rotinas e bases que precisam ser atualizadas todo mês: o que é, de onde vem, quando sai e para quem vai."),
    ("p11", "Delta · Onboarding e kit", "Kit Delta, carta do executivo, proposta e jornada dos dois anos."),
]

# (projeto, seção, título, status, prioridade, entregável, link, notas)
T = [
 # P0
 ("p0","Pessoas","Definir sucessor(a) para cada frente (base, página, cartas, treinamento, documentação)","A fazer","Alta","Matriz de responsáveis preenchida neste quadro","", "Preencher o campo Sucessor(a) em cada tarefa. Filtro 'Sem sucessor' mostra o que falta."),
 ("p0","Pessoas","Reunião de kickoff do repasse com o time de R&S","A fazer","Alta","Ata com responsáveis e datas","", "Apresentar este quadro, combinar rotina de acompanhamento semanal até a data de saída."),
 ("p0","Parceiros","Agendar passagem de bastão com a InHire (Diego Guedes / Isabela Britto)","A fazer","Alta","Reunião realizada e novo ponto focal informado à InHire","", "diego.guedes@inhire.com.br (implantação/importação) · isabela.britto@inhire.com.br (materiais)."),
 ("p0","Acessos","Transferir acessos e propriedade de arquivos","A fazer","Alta","Novo(a) admin no InHire; arquivos do Drive transferidos","", "Perfil admin InHire, pastas de fotos, planilhas, formulários e materiais. Conferir quem é editor da Planilha v4."),
 ("p0","Comunicação","Comunicar Heads e gestores sobre o novo ponto focal de R&S/InHire","A fazer","Média","E-mail enviado aos Heads de cada empresa","", "Usar a lista de Heads da aba 'Opções de resposta em lista'."),

 # P1 – base
 ("p1","LOTE 1 · Vagas abertas/congeladas","Preencher 'Gestor Imediato' (coluna G)","A fazer","Alta","Coluna G completa, nomes iguais à lista de opções",PLANILHA,"Comentário do Diego (30/09): inserir gestor imediato. Corrigir quebras de linha nos nomes (ex.: ADILSON NONATO DO NASCIMENTO)."),
 ("p1","LOTE 1 · Vagas abertas/congeladas","Revisar 'Tipo de Contratação' (coluna AC) marcada como pendente","A fazer","Alta","Coluna AC validada",PLANILHA,"Opções: CLT, PJ, Contrato temporário, Associado, Autônomo, Cooperado, Estágio, Menor aprendiz."),
 ("p1","LOTE 1 · Vagas abertas/congeladas","Completar 'Descritivo da Vaga' (coluna AS) e 'Nome externo de divulgação'","A fazer","Média","Descritivos preenchidos ou N/A justificado",PLANILHA,"Diego sinalizou a coluna AS (30/09). Hoje há links do gupy.io que vão expirar com a migração."),
 ("p1","LOTE 1 · Vagas abertas/congeladas","Informar a escala da vaga 10222 (Assist. Crédito em Conta – IFP Uberaba)","A fazer","Média","Escala preenchida conforme lista (F32, F57...)",PLANILHA,"Comentário 'faltou escala' na célula AE4."),
 ("p1","LOTE 1 · Vagas abertas/congeladas","Validar 'Cliente' e 'Tipo de Contrato' contra as listas de opções","A fazer","Média","Valores padronizados",PLANILHA,"Cliente/Squad: Loja, Tecnologia, Corporativo. Hoje o Tipo de Contrato está como 'EFETIVO', que não existe na lista (Contrato determinado/indeterminado)."),
 ("p1","LOTE 2 · Fechadas/canceladas","Corrigir 'Tipo de processo' (coluna AA)","A fazer","Alta","Coluna AA com opções válidas",PLANILHA,"Hoje está 'CLT'. Opções: Recrutamento Interno, Recrutamento Externo, Indicação do Gestor Durante o Processo, Candidato Definido, Efetivação Aprendiz e Estag."),
 ("p1","LOTE 2 · Fechadas/canceladas","Corrigir 'Tipo de movimentação' (coluna AB)","A fazer","Alta","Coluna AB com opções válidas",PLANILHA,"Hoje está 'CONTRATO DETERMINADO'. Opções: Admissão de colaborador, Contratação sem vínculo, Recontratação de ex-colaborador, Transferência interna, Movimentação de colaborador, Recrutamento Interno."),
 ("p1","LOTE 2 · Fechadas/canceladas","Identificar colaborador substituído nas vagas de substituição","A fazer","Média","Campo 'Colaborador Substituído' preenchido",PLANILHA,"Pergunta aberta do Diego: 'não sabemos quem é a pessoa substituída aqui?'."),
 ("p1","LOTE 2 · Talentos contratados","Confirmar que 'Data Contratação' = data de admissão e replicar nas vagas fechadas","A fazer","Média","Datas conferidas nas duas abas",PLANILHA,"Comentário na célula M2."),
 ("p1","LOTE 2 · Talentos contratados","Conferir se os IDs batem com a aba 'LOTE 2 – Vagas Fechadas/Canceladas'","A fazer","Alta","IDs 100% conciliados",PLANILHA,"Requisito da importação: ID do talento = ID da vaga fechada."),
 ("p1","Padronização","Trocar 'Segmento' por 'Head' usando só o nome da área","Em andamento","Média","Lista de Heads padronizada",PLANILHA,"Diego: manter só a área (incluir nome de pessoas gera manutenção). Consultar a Thay se dá para tratar a resposta pegando só o que vem depois do '-'. Falta subir a carga de respostas."),
 ("p1","Padronização","Revisar dados pessoais (CPF) compartilhados na planilha","A fazer","Alta","Acesso restrito e só os campos necessários à carga",PLANILHA,"LGPD: a aba de talentos tem CPF. Limitar editores e apagar após a importação."),
 ("p1","Entrega","Consolidar a base final com todas as vagas e enviar à InHire","Em andamento","Alta","Base final preenchida e validada pelo Diego",PLANILHA,"Versão vigente: v4 (v2 está obsoleta). Hoje há 3 vagas no LOTE 1 e 5 no LOTE 2; confirmar se é amostra ou o total."),
 ("p1","Entrega","Validar a carga no InHire após a importação","A fazer","Alta","Checagem por amostragem sem divergências",PLANILHA,"Conferir requisições, vagas, recrutador, gestor e status no ambiente InHire."),

 # P2 – página
 ("p2","Conteúdo","Selecionar as fotos do RH (setembro/26)","Em andamento","Média","Fotos escolhidas e tratadas",FOTOS,"Pastas 'FOTOS DAYCOVAL - RH SETEMBRO 26' e 'FOTOS' no Drive."),
 ("p2","Conteúdo","Revisar textos institucionais (sobre, cultura, benefícios, empresas do grupo)","A fazer","Média","Textos aprovados","","Validar com Marketing/Comunicação."),
 ("p2","Configuração","Montar a página de carreiras no InHire","A fazer","Alta","Página publicada em homologação","","Inclui identidade visual, seções e filtros por empresa/área."),
 ("p2","Configuração","Substituir links das vagas do gupy.io pelos links do InHire","A fazer","Média","Links atualizados nos canais (site, LinkedIn)","","Os links atuais de Daycoval, Daycoval Tech e Daycred no gupy.io deixam de funcionar ao desligar a Gupy."),
 ("p2","Aprovação","Aprovação final e publicação da página","A fazer","Alta","Página no ar","","Aprovação RH + Marketing."),

 # P3 – cartas
 ("p3","Modelos","Redigir modelos de carta proposta por tipo de contratação","Em andamento","Alta","Modelos CLT, Estágio e Aprendiz","","Campos dinâmicos: nome, cargo, empresa, salário contratual, escala, data de admissão, benefícios."),
 ("p3","Modelos","Validar os modelos com DP e Jurídico","A fazer","Alta","Modelos aprovados","",""),
 ("p3","Configuração","Configurar as cartas no InHire com variáveis e fluxo de aprovação","A fazer","Alta","Modelos ativos no InHire","","Definir quem aprova a proposta antes do envio ao talento."),
 ("p3","Configuração","Testar o envio de proposta de ponta a ponta","A fazer","Média","Teste aprovado","","Uma vaga de teste por tipo de contratação."),

 # P4 – treinamento
 ("p4","Lideranças","Adaptar o Manual de Lideranças da InHire à realidade Daycoval","Em andamento","Alta","Manual adaptado",MANUAL,"Módulos: visão geral da vaga, o candidato na vaga, Kit Entrevista, Analytics da vaga."),
 ("p4","Lideranças","Agendar e aplicar o treinamento de gestores","A fazer","Alta","Turmas realizadas e lista de presença","","Fernanda está desenvolvendo um treinamento para líderes. Alinhar o conteúdo para não duplicar."),
 ("p4","Time de R&S","Treinar o time de R&S no fluxo InHire (etapas, feedback, encerramento)","A fazer","Alta","Treinamento aplicado e gravado","","Atacar as dores da Gupy: pular etapas, feedback atrasado, vagas com +90 dias abertas."),
 ("p4","Programa de Indicação","Planejar a implantação do Programa de Indicação","A fazer","Média","Cronograma e comunicação aos membros internos",INDICACAO,"Material de apoio da InHire para recrutador e membro interno."),
 ("p4","Acervo","Centralizar gravações e materiais numa pasta compartilhada","A fazer","Média","Pasta organizada com link no quadro","",""),

 # P5 – documentação
 ("p5","Processos","Documentar o fluxo de requisição e aprovação de vagas","A fazer","Alta","Fluxo documentado","","Tipos de requisição: aumento de quadro, aumento temporário, substituição. Requisição sigilosa."),
 ("p5","Processos","Documentar SLA por nível e regras de encerramento de vagas","A fazer","Média","Política publicada","","Operacionais 20 dias · Analistas/Especialistas 30 dias · Gestão 40 dias."),
 ("p5","Governança","Mapa de perfis e permissões no InHire","A fazer","Alta","Tabela perfil x permissão","","Recrutador, gestor, avaliador, admin, RH."),
 ("p5","Governança","Dicionário de campos personalizados (requisição e vaga)","A fazer","Média","Dicionário publicado",PLANILHA,"Base: aba 'Mapeamento de Campos' da Planilha v4."),
 ("p5","Governança","Registrar dores da Gupy e como o InHire resolve cada uma","A fazer","Baixa","Quadro comparativo",GUPY,"Planilha 'Banco Daycoval e Gupy – Mapeamento de melhorias'."),
 ("p5","Contatos","Registrar contatos, suporte e rotinas com a InHire","A fazer","Média","Página de contatos","","Implantação: Diego Guedes. Materiais/CS: Isabela Britto."),

 # P6 – Delta: estratégia
 ("p6","Estratégia","Validar KV e naming do Programa Delta","Em andamento","Alta","KV aprovado","","O KV está 'em validação' no deck. Conceito: os 4 Ds (Desafio, Descoberta, Desenvolvimento, Desempenho)."),
 ("p6","Estratégia","Confirmar as 11 vagas por área e o gestor de cada uma","A fazer","Alta","Quadro de vagas assinado pelos gestores","","Captação 2 (Jayme Carvalho) · Daycoval Invest 2 (Adriana Siebert) · DCM 1 (Renato Otranto) · Tesouraria 2 (Paulo Saba) · Asset 1 (Roberto Kropp) · Serviços Fiduciários 2 (Eric de Carvalho) · Riscos e Compliance 1 (Adely)."),
 ("p6","Estratégia","Alinhar a meta do funil com o número de vagas","A fazer","Alta","Meta de funil revisada","","O deck traz 11 vagas, mas o funil de seleção termina em 8 selecionados (100–130 ativados → 40 no Challenge → 8). Ajustar uma das duas pontas."),
 ("p6","Orçamento","Fechar orçamento de atração e seleção","A fazer","Alta","Orçamento aprovado","","Cia de Estágios: R$ 2,8 mil por vaga no sucesso (11 vagas ≈ R$ 30,8 mil) + R$ 20,5 mil em ações de atração. Total ≈ R$ 51,3 mil, sem o Kit Delta e eventos."),
 ("p6","Fornecedor","Contratar a Cia de Estágios (proposta, contrato e SLA)","A fazer","Alta","Contrato assinado",CIA,"Escopo: marketing dedicado, hotsite, divulgação multicanal, banco de talentos e entrevistas comportamentais com feedback."),
 ("p6","Cronograma","Montar o cronograma macro da atração até a admissão","A fazer","Alta","Cronograma com datas de cada etapa","","Cruzar com o calendário acadêmico das target (provas, férias, semanas de carreira)."),
 ("p6","Aprovação","Aprovação executiva do programa","A fazer","Alta","Escopo, orçamento e cronograma aprovados","",""),

 # P7 – universidades e contatos
 ("p7","Target","Fechar a lista de universidades target e cursos","Em andamento","Alta","Lista final de instituições e cursos","","Deck: USP, FGV, Insper, ITA, Link School of Business e federais (definir quais). Unicamp aparece nos números da Cia. Cursos: Administração, Economia, Matemática, Engenharias, Tecnologia, Física."),
 ("p7","Contatos","Mapear contatos de cada universidade (centro de carreiras, empresa júnior, ligas)","A fazer","Alta","Aba Universidades preenchida com nome, e-mail e telefone","","Priorizar ligas de mercado financeiro e empresas júnior, que fazem a ponte com os alunos."),
 ("p7","Contatos","Fazer o primeiro contato e apresentar o Delta a cada universidade","A fazer","Alta","Status 'Contato feito' em todas as target","","Registrar o retorno e a próxima ação na aba Universidades."),
 ("p7","Calendário","Levantar o calendário acadêmico e as semanas de carreira","A fazer","Média","Calendário consolidado por instituição","","Evitar provas e férias nas datas de palestra e do Challenge Day."),
 ("p7","Banco de talentos","Ativar o banco de talentos da Cia de Estágios nas target","A fazer","Média","Lista de candidatos ativados",CIA,"Referência do deck: Insper +2.500 · FGV +3.500 · USP +34.200 · Unicamp +14.500 · ITA +100."),
 ("p7","Indicações","Coletar indicações de gestores e estagiários atuais","A fazer","Média","Lista de indicados","","Usar o Programa de Indicação do InHire, se já estiver ativo."),

 # P8 – palestras e ativações
 ("p8","Palestras","Definir formato e roteiro padrão da palestra Delta","A fazer","Alta","Roteiro e apresentação prontos","","Quem fala, duração, case do mercado financeiro, depoimento de estagiário e CTA para a inscrição."),
 ("p8","Palestras","Escalar executivos e gestores para as palestras","A fazer","Alta","Agenda de palestrantes por universidade","","Os gestores das 7 áreas são o primeiro grupo a convidar."),
 ("p8","Palestras","Agendar as palestras nas universidades target","A fazer","Alta","Palestras confirmadas na aba Universidades","","Status 'Palestra agendada' com data em cada instituição."),
 ("p8","Ativações","Organizar o 'Portas abertas' no Daycoval","A fazer","Média","Evento realizado","","Visita dos universitários ao banco, com conversa com as áreas."),
 ("p8","Ativações","Avaliar participação em feiras de carreira patrocinadas","A fazer","Baixa","Decisão e orçamento","",""),
 ("p8","Ativações","Montar o mailing via WhatsApp a partir das ativações","A fazer","Média","Lista com consentimento registrado","","Origem: banco de talentos e empresas júnior. LGPD: guardar o consentimento de cada contato."),
 ("p8","Medição","Registrar presença e inscrições geradas por ação","A fazer","Média","Planilha de conversão por ação e universidade","","Mede quais palestras e canais trazem candidatos para o funil."),

 # P9 – marca e divulgação
 ("p9","Divulgação","Hotsite do Delta com a Cia de Estágios","A fazer","Alta","Hotsite no ar",CIA,"Exemplos citados no deck: hotsites da Pátria e do Banco ABC na Cia de Estágios."),
 ("p9","Divulgação","Produzir os materiais de divulgação","A fazer","Alta","Cards, cartaz digital para faculdades, posts de lançamento e encerramento","",""),
 ("p9","Divulgação","Plano de mídia orgânica e patrocinada","A fazer","Média","Plano por canal com datas","","Canais: TikTok, Telegram, WhatsApp, X/Twitter e LinkedIn. Inclui imprensa e destaque na home da Cia."),
 ("p9","Divulgação","Alinhar campanha com Marketing e Comunicação interna","A fazer","Média","Calendário aprovado","",""),
 ("p9","Divulgação","Publicar a vaga Delta no InHire e na página de carreiras","A fazer","Alta","Vaga publicada com link do hotsite","","Depende do projeto Página de carreiras."),

 # P10 – seleção
 ("p10","Configuração","Configurar as etapas do Delta no InHire","A fazer","Alta","Fluxo configurado","","Inscrição → testes → entrevista Cia → live → Challenge Day → entrevistas finais → proposta."),
 ("p10","Testes","Definir e configurar os testes","A fazer","Alta","Testes ativos","","Raciocínio lógico, inglês (certificações), Assessment Learning Agility, fit cultural e vídeo 'Por que devemos te contratar?'."),
 ("p10","Entrevistas","Entrevistas comportamentais com a Cia de Estágios","A fazer","Média","Pareceres e feedbacks individuais",CIA,""),
 ("p10","Preparação","Live privada de preparação para o Challenge Day","A fazer","Média","Live realizada","","Formato educacional, para os candidatos chegarem preparados."),
 ("p10","Preparação","Preparar os gestores para conduzir o Challenge Day","A fazer","Alta","Gestores treinados e com roteiro de avaliação","",""),
 ("p10","Challenge Day","Criar o business case transversal e a banca","A fazer","Alta","Case e critérios de avaliação","","Case único para todas as áreas, com pitch dos grupos."),
 ("p10","Challenge Day","Logística do Challenge Day","A fazer","Alta","Evento pronto","","2 dias com 20 candidatos por dia: dinâmica com executivos, brunch/coffee de networking, case e pitch."),
 ("p10","Final","Entrevistas finais com gestores e feedbacks individuais","A fazer","Alta","Aprovados definidos","",""),

 # P11 – onboarding
 ("p11","Kit","Produzir o Kit Delta","A fazer","Média","Kits entregues","","Mochila, jaqueta, caderno premium, caneta executiva, garrafa térmica, pin metálico e itens de identidade."),
 ("p11","Kit","Solicitar os notebooks corporativos à TI","A fazer","Média","Equipamentos prontos na admissão","",""),
 ("p11","Kit","Carta de boas-vindas assinada pelo executivo","A fazer","Baixa","Cartas assinadas","",""),
 ("p11","Admissão","Proposta e contrato de estágio","A fazer","Alta","Propostas aceitas","","Usa os modelos de carta proposta de estágio (projeto Cartas proposta)."),
 ("p12","Inventário","Listar todas as bases mensais e rotinas recorrentes","A fazer","Alta","Lista com nome, periodicidade, prazo, fonte e destinatário","","Ex.: indicadores de R&S, vagas abertas/fechadas, SLA, headcount. Cadastrar cada base como uma tarefa nesta seção."),
 ("p12","Passo a passo","Documentar o passo a passo de cada base","A fazer","Alta","Procedimento por base, com prints e onde salvar","","Inclui de onde extrair (InHire, LG, planilhas), tratamentos e quem recebe."),
 ("p12","Transição","Fazer a próxima atualização mensal junto com o(a) sucessor(a)","A fazer","Alta","Uma rodada completa feita a quatro mãos","",""),
 ("p11","Jornada","Detalhar a jornada dos 2 anos","A fazer","Média","Calendário da jornada aprovado","","Ano 1: 3 meses na área de origem, soft skills (3 módulos), hard skills, job rotation, encontro com RH. Ano 2: projeto aplicado, hard e soft skills, encontro com RH. Ao longo: mentoria dirigida, conexão ESG, encontro com diretores. Rede Alumni ao final."),
]

UNIS = [
    ("USP", "+34.200 cadastros na Cia de Estágios", "Administração, Economia, Engenharias, Matemática, Física"),
    ("FGV", "+3.500 cadastros ativos", "Administração, Economia, Matemática Aplicada"),
    ("Insper", "+2.500 cadastros (Engenharias +500)", "Administração, Economia, Engenharias, Ciência da Computação"),
    ("ITA", "+100 candidatos disponíveis", "Engenharias, Computação"),
    ("Unicamp", "+14.500 cadastros (Eng. Produção +700)", "Economia, Engenharias, Matemática, Física"),
    ("Link School of Business", "", "Administração, Economia"),
    ("Universidades federais (definir quais)", "", "A definir"),
]
CANAIS = ["Centro de carreiras", "Empresa júnior", "Liga / entidade estudantil"]
contacts = []
for i,(inst,reach,courses) in enumerate(UNIS):
    for j,ch in enumerate(CANAIS):
        contacts.append(dict(id=f"c{i+1}{j+1}", inst=inst, reach=reach, channel=ch, name="", role="", email="", phone="",
                             status="Mapear contato", owner="", next="Mapear contato", date="", courses=courses, notes="", order=(i+1)*10+j))

tasks = []
order = {}
for i,(p,sec,title,status,prio,deliv,link,notes) in enumerate(T):
    order[p] = order.get(p,0)+1
    tasks.append(dict(id=f"t{i+1:02d}", project=p, section=sec, title=title, status=status, handover=SIT[SITUACAO[i]], doneAt="", priority=prio,
                      owner=ATUAL, successor=SUC, due="", deliverable=deliv, link=link, notes=notes, order=order[p]))

assert len(SITUACAO) == len(T)
ORDEM = ["p0","p12","p1","p3","p2","p4","p5","p6","p7","p8","p9","p10","p11"]
proj = sorted([dict(id=pid, name=n, type=TIPOS[pid], desc=d, order=ORDEM.index(pid)) for (pid,n,d) in projects], key=lambda p: p["order"])
(HERE/"tarefas.json").write_text(json.dumps({"projects":proj,"tasks":tasks,"contacts":contacts}, ensure_ascii=False, indent=2))

pname = {p["id"]:p["name"] for p in proj}
ptype = {p["id"]:p["type"] for p in proj}
with open(HERE/"asana_import.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Name","Section/Column","Tipo de projeto","Assignee","Due Date","Description","Status","Situação no repasse","Concluída em","Prioridade","Responsável atual","Sucessor(a)","Entregável","Link"])
    for t in tasks:
        desc = f"Entregável: {t['deliverable']}\n{t['notes']}" + (f"\nLink: {t['link']}" if t['link'] else "")
        w.writerow([t["title"], f"{pname[t['project']]} · {t['section']}", ptype[t["project"]], "", t["due"], desc, t["status"], t["handover"], t["doneAt"], t["priority"], t["owner"], t["successor"], t["deliverable"], t["link"]])
with open(HERE/"delta_universidades.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Instituição","Alcance (Cia de Estágios)","Canal","Contato","E-mail","Telefone","Status","Próxima ação","Responsável","Cursos"])
    for c in contacts:
        w.writerow([c["inst"],c["reach"],c["channel"],"","","",c["status"],c["next"],"",c["courses"]])
print(len(proj), "projetos,", len(tasks), "tarefas,", len(contacts), "contatos")
