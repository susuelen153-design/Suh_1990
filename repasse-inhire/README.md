# Repasse InHire – R&S Daycoval

Estrutura no estilo Asana para o repasse da implantação do InHire: 7 projetos (agrupados por tipo) e 40 tarefas, com entregável, status, prioridade, responsável atual e sucessor(a).

| Arquivo | Para que serve |
|---|---|
| `build_data.py` | Fonte única dos projetos e tarefas. Edite aqui e rode `python3 build_data.py`. |
| `tarefas.json` | Projetos e tarefas gerados (base do quadro online). |
| `asana_import.csv` | Importação direta no Asana: Novo projeto → Importar → CSV. Cada "Section/Column" vira uma seção. |
| `delta_universidades.csv` | Universidades target do Delta × canal, para preencher contatos. |
| `quadro-repasse.html` | Página do quadro compartilhado, em tema escuro: Projetos por tipo com medição, Lista, Quadro por status e Matriz de responsáveis. |

## Projetos por tipo
- **Gestão do repasse:** Transição e governança
- **Manutenção:** Bases mensais (inventário, passo a passo, rodada junto com o sucessor)
- **InHire · Nova ATS:** Etapa 1 Base final preenchida → Etapa 2 Cartas proposta → Etapa 3 Página de carreiras → Etapa 4 Treinamento → Etapa 5 Documentação
- **Programa Delta (estágio):** Estratégia e orçamento → Universidades e contatos → Palestras e ativações → Marca e divulgação → Seleção e Challenge Day → Onboarding e kit

Cada tarefa tem a situação no repasse: **Atualizar**, **Manter**, **Criar** ou **A avaliar**. As concluídas continuam no quadro com a data de conclusão, para medir o andamento.

A aba **Universidades** do quadro registra os contatos das target do Delta (USP, FGV, Insper, ITA, Unicamp, Link School of Business e federais) por canal: centro de carreiras, empresa júnior e ligas. `delta_universidades.csv` é a mesma lista para planilha.

As pendências da Etapa 1 vêm dos comentários abertos do Diego Guedes (InHire) na Planilha de Importação v4. As tarefas do Delta vêm do deck "Programa Delta".
