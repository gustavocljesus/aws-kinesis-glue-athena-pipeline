## Descrição
Este projeto implementa uma arquitetura de Data Lake na AWS para ingestão, processamento e consulta de dados simulados de uma fazenda eólica, utilizando streaming em tempo quase real.

## Objetivo
- Simular dados de uma fazenda eólica
- Coletar dados via streaming
- Converter os dados para parquet com um processo de ETL
- Fazer consultas com os dados tratados

## Tecnologias Utilizadas
- Python
- Amazon Kinesis Data Streams
- Amazon Data Firehose
- Amazon S3
- AWS Glue
- Amazon Athena

## Conceitos Aplicados
- Arquitetura Data Lake
- Streaming de dados
- ETL em ambiente distribuído
- Armazenamento em formato columnar (Parquet)
- Particionamento para otimização de consultas

## Arquitetura
![Data Pipeline Architecture](docs/data-pipeline-architecture.svg)

## Fluxo da Pipeline
1. Produtores Python simulam dados de sensores
2. Os dados são enviados para o Amazon Kinesis Data Streams
3. O Amazon Data Firehose entrega os dados no S3 (camada raw)
4. Um job no AWS Glue transforma os dados para formato Parquet
5. Os dados tratados são particionados e disponibilizados para consulta no Amazon Athena

## Camadas do Data Lake
- Raw: dados brutos recebidos via streaming
- Processed: dados transformados para Parquet e particionados por tipo

## Estrutura do Projeto
```text
project-pipeline/
├── docs/
│   ├── data-pipeline-architecture.svg
│   └── glue_visual_ETL.png
├── src/
│   ├── athena/
│   │    └── analytics_queries/
│   │        └── registro_intervalo_datas.sql
│   ├── glue/
│   │   └── jobWindFarm.py
│   ├── producer/
│   │   ├── hydraulic_prepressure.py
│   │   ├── power_factor.py
│   │   └── temperature_battery.py
│   └── streaming/
│       └── kinesis_writer.py
├── main.py
├── .env
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt

s3://my-pipeline-engdados-project/
├── data-lake/
│    ├── raw/
│    │   └── kinesis/
│    │       └── 2026/...
│    └── processed/
│        └── glue/
│            └── type=.../

s3://aws-assets-my-bucket/
├── scripts/
├── logs/
├── temp/
└── queries-athena/
```
**Observação:** o particionamento será feito pelo Amazon Data Firehose e o AWS Glue.

## Base de Dados
Os dados são simulados por produtores Python que representam sensores de uma fazenda eólica, como:
- Temperatura da bateria
- Fator de potência
- Pressão hidráulica

Os dados são gerados em tempo quase real e enviados via streaming.

## Consultas SQL
**Registro em um intervalo de datas:** registro dos dados em um intervalo de tempo predefinido, organizado pelos tipos de dados coletados.

## Como Executar
1. Criar um fluxo de dados no Amazon Kinesis Data Streams
2. Criar um fluxo do Firehose no Amazon Data Firehose
    - Nesta etapa o intervalo do buffer foi definido para 60 segundos.
3. Instalar dependências: 
    - `pip install -r requirements.txt`
4. Executar o script `main.py`
    - As configurações do AWS foram definidas via CLI no `aws configure`
    - Alternativamente, as credenciais podem ser configuradas diretamente no `boto3.client()`
5. Criar uma role IAM para o AWS Glue com políticas que permitam acesso ao S3, Glue Data Catalog e execução do job.
6. Criar um database em AWS Glue
7. Criar um crawler em  AWS Glue
8. Criar um Visual ETL Job semelhante ao `glue_visual_ETL.png` disponível em `docs/` ou executar o script `jobWindFarm.py` disponível em `src/glue/`
    - **Observação:** caso utilize `jobWindFarm.py`, ajuste previamente os parâmetros do job. 
    - As dependências do script são providas pelo ambiente gerenciado do AWS Glue.
9. Executar `registro_intervalo_datas.sql` disponível em `src/athena/analytics_queries/` no Amazon Athena

## Melhorias Futuras
- Os dados produzidos são alguns dos dados gerados em uma fazenda eólica. Para uma simulação mais próxima do real, seria necessário produzir os outros tipos de dados.
- Como o projeto é simulado, o volume de dados é reduzido. Em um cenário real, a consulta presente no projeto poderia ser estendida com funções analíticas para:
    - cálculo de médias móveis
    - detecção de outliers
    - identificação automática de coletas fora do padrão esperado