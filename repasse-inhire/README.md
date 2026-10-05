# Repasse InHire – R&S Daycoval

Estrutura no estilo Asana para o repasse da implantação do InHire: 7 projetos (agrupados por tipo) e 40 tarefas, com entregável, status, prioridade, responsável atual e sucessor(a).

| Arquivo | Para que serve |
|---|---|
| `build_data.py` | Fonte única dos projetos e tarefas. Edite aqui e rode `python3 build_data.py`. |
| `tarefas.json` | Projetos e tarefas gerados (base do quadro online). |
| `asana_import.csv` | Importação direta no Asana: Novo projeto → Importar → CSV. Cada "Section/Column" vira uma seção. |
| `quadro-repasse.html` | Página do quadro compartilhado, em tema escuro: Projetos por tipo com medição, Lista, Quadro por status e Matriz de responsáveis. |

## Projetos
0. Transição e governança do repasse
1. Base final preenchida (Planilha de Importação v4, com a InHire)
2. Página de carreiras
3. Cartas proposta
4. Material de treinamento
5. Documentação InHire
6. Delta – programa de estágio

Cada tarefa tem a situação no repasse: **Atualizar** (existe, mas precisa ser revisada), **Manter** (repassar como está), **Criar** (ainda não existe) ou **A avaliar**. As concluídas continuam no quadro com a data de conclusão, para medir o andamento.

As pendências do projeto 1 vêm dos comentários abertos do Diego Guedes (InHire) na Planilha de Importação v4.
