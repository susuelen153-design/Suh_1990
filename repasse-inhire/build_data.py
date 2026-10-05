"""Fonte única do repasse InHire: gera tarefas.json (quadro) e asana_import.csv (importação no Asana)."""
import csv, json, pathlib

HERE = pathlib.Path(__file__).parent
ATUAL = "Suellen Pereira da Silva"
SUC = ""  # sucessor(a) a definir no quadro

PLANILHA = "https://docs.google.com/spreadsheets/d/18XiwQr1AXpgs___fAk0nZDhYA5YvfpuokPxGPwHCTSE/edit"
FOTOS = "https://drive.google.com/drive/folders/1LdBZK69yVizn_WxvufqKtcIZsw4NvMR-"
MANUAL = "https://drive.google.com/file/d/19x416s7mUmxWs2ARTMga5m1RzBaG8huX/view"
INDICACAO = "https://drive.google.com/file/d/1p92SYhUJW0iSi7IKYZc9DwLgAq4t2YPp/view"
GUPY = "https://docs.google.com/spreadsheets/d/1P8T1nctioHdNWqfhKaIlwD-fsDWVgiOgNpdBD180BF8/edit"

TIPOS = {"p0":"Gestão do repasse","p1":"Implantação do sistema","p3":"Implantação do sistema","p2":"Comunicação e marca",
         "p4":"Capacitação e documentação","p5":"Capacitação e documentação","p6":"Programas de atração"}

# Situação no repasse, na ordem das tarefas: A=Atualizar (existe, precisa revisar), M=Manter (repassa como está), C=Criar (não existe), V=A avaliar
SITUACAO = "CCCCC" + "AAAAAAAAAAAAAC" + "MACAC" + "ACCC" + "ACCVC" + "CCCAMC" + "V"
SIT = {"A":"Atualizar","M":"Manter","C":"Criar","V":"A avaliar"}

projects = [
    ("p0", "Transição e governança do repasse", "Organizar quem assume o quê, acessos e comunicação da saída."),
    ("p1", "Base final preenchida (importação)", "Planilha de Importação v4 com a InHire (Diego Guedes): LOTE 1 vagas abertas/congeladas, LOTE 2 fechadas/canceladas e talentos contratados."),
    ("p2", "Página de carreiras", "Página da Daycoval no InHire, com fotos do RH (set/26), textos e links das vagas."),
    ("p3", "Cartas proposta", "Modelos de carta proposta no InHire por tipo de contratação, com campos dinâmicos e aprovação."),
    ("p4", "Material de treinamento", "Treinamentos para lideranças, time de R&S e Programa de Indicação."),
    ("p5", "Documentação InHire", "Guia de processos, governança, SLAs e contatos para manter a operação sem a dona atual."),
    ("p6", "Delta", "Programa de estágio. Escopo, etapas e entregáveis a detalhar com quem conduz o programa."),
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

 # P6 – Delta (estágio)
 ("p6","Levantamento","Levantar o status do Programa Delta e registrar etapas e entregáveis pendentes","A fazer","Alta","Tarefas do Delta detalhadas neste quadro","","Cronograma, turma atual, gestores, processo seletivo, efetivações e cota."),
]

tasks = []
order = {}
for i,(p,sec,title,status,prio,deliv,link,notes) in enumerate(T):
    order[p] = order.get(p,0)+1
    tasks.append(dict(id=f"t{i+1:02d}", project=p, section=sec, title=title, status=status, handover=SIT[SITUACAO[i]], doneAt="", priority=prio,
                      owner=ATUAL, successor=SUC, due="", deliverable=deliv, link=link, notes=notes, order=order[p]))

assert len(SITUACAO) == len(T)
proj = [dict(id=pid, name=n, type=TIPOS[pid], desc=d, order=k) for k,(pid,n,d) in enumerate(projects)]
(HERE/"tarefas.json").write_text(json.dumps({"projects":proj,"tasks":tasks}, ensure_ascii=False, indent=2))

pname = {p["id"]:p["name"] for p in proj}
ptype = {p["id"]:p["type"] for p in proj}
with open(HERE/"asana_import.csv","w",newline="",encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Name","Section/Column","Tipo de projeto","Assignee","Due Date","Description","Status","Situação no repasse","Concluída em","Prioridade","Responsável atual","Sucessor(a)","Entregável","Link"])
    for t in tasks:
        desc = f"Entregável: {t['deliverable']}\n{t['notes']}" + (f"\nLink: {t['link']}" if t['link'] else "")
        w.writerow([t["title"], f"{pname[t['project']]} · {t['section']}", ptype[t["project"]], "", t["due"], desc, t["status"], t["handover"], t["doneAt"], t["priority"], t["owner"], t["successor"], t["deliverable"], t["link"]])
print(len(proj), "projetos,", len(tasks), "tarefas")
