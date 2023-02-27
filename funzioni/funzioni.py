

def run_dataq(expectation_suite_name='Main'):
    import os
    import pandas as pd
    import datetime
    from datetime import date
    import re
    from ruamel import yaml
    from ruamel.yaml import YAML
    ## Ge
    import great_expectations as gx


    yaml = YAML()
    context = gx.get_context()
    expectation_suite_name = 'Main'
    path = '../data'
    regex = r'scraping_all_[0-9]{8}'
    print('Questa la documentazione sulla suite:',expectation_suite_name, '\n', 'http://localhost:9000/view/great_expectations/uncommitted/data_docs/local_site/expectations/'+ expectation_suite_name +'.html')
    for e in os.listdir(path):
        if re.match(regex, e):
            file_path = path + '/' + e
            my_checkpoint_name = 'checkpoint_' + e[13:-4]
            data_asset_name = e[:-4]
            yaml_config = f"""
                            name: {my_checkpoint_name}
                            config_version: 1.0
                            class_name: SimpleCheckpoint
                            run_name_template: "%Y%m%d-%H%M%S-{data_asset_name}"
                            validations:
                              - batch_request:
                                  datasource_name: glassdoor_scraping 
                                  data_connector_name: all
                                  data_asset_name: {data_asset_name}
                                  data_connector_query:
                                    index: -1
                                expectation_suite_name: {expectation_suite_name}
                            """
            context.add_or_update_checkpoint(**yaml.load(yaml_config))
            results = context.run_checkpoint(checkpoint_name=my_checkpoint_name, expectation_suite_name = 'Main')
            a = re.findall('[0-9]{8}-[0-9]{6}-' + data_asset_name + '/[0-9]{8}T[0-9]{6}.[0-9]{6}Z/[\S]{32}', str(list(results['run_results'])[0]))[0]
            b = expectation_suite_name + '/' + a
            print(f'Consulta i risultati del data_asset_name "{data_asset_name}" al link:\n' + "http://localhost:9000/view/great_expectations/uncommitted/data_docs/local_site/validations/" + b + '.html')
    print('Checkpoint aggiornati o aggiunti:\n', context.list_checkpoints())

def parse_json():   
    import json
    import os
    import sys
    import re
    import pandas as pd
    sys.path.append('../../')
    path = "../great_expectations/uncommitted/validations/Main"
    expectation_type=[]
    dataframe_type=[]
    expectation_type=[]
    element_count=[]
    missing_count=[]
    missing_percent=[]
    partial_unexpected_counts=[]
    partial_unexpected_index_list=[]
    partial_unexpected_list=[]
    unexpected_count=[]
    unexpected_percent=[]
    unexpected_percent_nonmissing=[]
    unexpected_percent_total=[]
    column=[]
    column_list=[]
    success=[]
    timestamp_run=[]
    
    
    for root, dirs, files in os.walk(path):
        for file in files:
            path_data = os.path.join(root, file)
            #escraping_date=re.search(regex1, path_data).group(1)
            
            with open(path_data, "r") as read_file:
                data = json.load(read_file)
                str_dataframe_type = data['meta']['active_batch_definition']['data_asset_name']
                str_timestamp_run = data['meta']['batch_markers']['ge_load_time']
                        
                    
                for e in data['results']:
                    for i in range(4):
                        dataframe_type.append(str_dataframe_type)
                        timestamp_run.append(str_timestamp_run)
                    
                    
                    

                    
                    try:
                        expectation_type.append(e['expectation_config']['expectation_type'])
                    except:
                        expectation_type.append(None)

                    try:
                        column.append(e['expectation_config']['kwargs']['column'])
                    except:
                        column.append(e['expectation_config']['kwargs']['column_list'][0])    
                    try:
                        column_list.append(e['expectation_config']['kwargs']['column_list'])
                    except:
                        column_list.append(None)          
                    try:
                        element_count.append(e['result']['element_count'])
                    except:
                        element_count.append(None)
                    try:
                        missing_count.append(e['result']['missing_count'])
                    except:
                        missing_count.append(None)
                    try:
                        missing_percent.append(e['result']['missing_percent'])
                    except:
                        missing_percent.append(None)
                    try:
                        partial_unexpected_counts.append(e['result']['partial_unexpected_counts'])
                    except:
                        partial_unexpected_counts.append(None)
                    try:
                        partial_unexpected_index_list.append(e['result']['partial_unexpected_index_list'])
                    except:
                        partial_unexpected_index_list.append(None)
                    try:
                        partial_unexpected_list.append(e['result']['partial_unexpected_list'])
                    except:
                        partial_unexpected_list.append(None)
                    try:
                        unexpected_count.append(e['result']['unexpected_count'])
                    except:
                        unexpected_count.append(None)
                    try:
                        unexpected_percent.append(e['result']['unexpected_percent'])
                    except:
                        unexpected_percent.append(None)
                    try:
                        unexpected_percent_nonmissing.append(e['result']['unexpected_percent_nonmissing'])
                    except:
                        unexpected_percent_nonmissing.append(None)
                    try:
                        unexpected_percent_total.append(e['result']['unexpected_percent_total'])
                    except:
                        unexpected_percent_total.append(None)
                    try:
                        expectation_type.append(e['expectation_config']['expectation_type'])
                    except:
                        expectation_type.append(None)
                    try:
                        column.append(e['expectation_config']['kwargs']['column'])
                    except:
                        column.append(e['expectation_config']['kwargs']['column_list'][0])    
                    try:
                        column_list.append(e['expectation_config']['kwargs']['column_list'])
                    except:
                        column_list.append(None)          
                    try:
                        element_count.append(e['result']['element_count'])
                    except:
                        element_count.append(None)
                    try:
                        missing_count.append(e['result']['missing_count'])
                    except:
                        missing_count.append(None)
                    try:
                        missing_percent.append(e['result']['missing_percent'])
                    except:
                        missing_percent.append(None)
                    try:
                        partial_unexpected_counts.append(e['result']['partial_unexpected_counts'])
                    except:
                        partial_unexpected_counts.append(None)
                    try:
                        partial_unexpected_index_list.append(e['result']['partial_unexpected_index_list'])
                    except:
                        partial_unexpected_index_list.append(None)
                    try:
                        partial_unexpected_list.append(e['result']['partial_unexpected_list'])
                    except:
                        partial_unexpected_list.append(None)
                    try:
                        unexpected_count.append(e['result']['unexpected_count'])
                    except:
                        unexpected_count.append(None)
                    try:
                        unexpected_percent.append(e['result']['unexpected_percent'])
                    except:
                        unexpected_percent.append(None)
                    try:
                        unexpected_percent_nonmissing.append(e['result']['unexpected_percent_nonmissing'])
                    except:
                        unexpected_percent_nonmissing.append(None)
                    try:
                        unexpected_percent_total.append(e['result']['unexpected_percent_total'])
                    except:
                        unexpected_percent_total.append(None)
                    try:
                        expectation_type.append(e['expectation_config']['expectation_type'])
                    except:
                        expectation_type.append(None)
                    try:
                        column.append(e['expectation_config']['kwargs']['column'])
                    except:
                        column.append(e['expectation_config']['kwargs']['column_list'][0])    
                    try:
                        column_list.append(e['expectation_config']['kwargs']['column_list'])
                    except:
                        column_list.append(None)          
                    try:
                        element_count.append(e['result']['element_count'])
                    except:
                        element_count.append(None)
                    try:
                        missing_count.append(e['result']['missing_count'])
                    except:
                        missing_count.append(None)
                    try:
                        missing_percent.append(e['result']['missing_percent'])
                    except:
                        missing_percent.append(None)
                    try:
                        partial_unexpected_counts.append(e['result']['partial_unexpected_counts'])
                    except:
                        partial_unexpected_counts.append(None)
                    try:
                        partial_unexpected_index_list.append(e['result']['partial_unexpected_index_list'])
                    except:
                        partial_unexpected_index_list.append(None)
                    try:
                        partial_unexpected_list.append(e['result']['partial_unexpected_list'])
                    except:
                        partial_unexpected_list.append(None)
                    try:
                        unexpected_count.append(e['result']['unexpected_count'])
                    except:
                        unexpected_count.append(None)
                    try:
                        unexpected_percent.append(e['result']['unexpected_percent'])
                    except:
                        unexpected_percent.append(None)
                    try:
                        unexpected_percent_nonmissing.append(e['result']['unexpected_percent_nonmissing'])
                    except:
                        unexpected_percent_nonmissing.append(None)
                    try:
                        unexpected_percent_total.append(e['result']['unexpected_percent_total'])
                    except:
                        unexpected_percent_total.append(None)
                    try:
                        expectation_type.append(e['expectation_config']['expectation_type'])
                    except:
                        expectation_type.append(None)
                    try:
                        column.append(e['expectation_config']['kwargs']['column'])
                    except:
                        column.append(e['expectation_config']['kwargs']['column_list'][0])    
                    try:
                        column_list.append(e['expectation_config']['kwargs']['column_list'])
                    except:
                        column_list.append(None)          
                    try:
                        element_count.append(e['result']['element_count'])
                    except:
                        element_count.append(None)
                    try:
                        missing_count.append(e['result']['missing_count'])
                    except:
                        missing_count.append(None)
                    try:
                        missing_percent.append(e['result']['missing_percent'])
                    except:
                        missing_percent.append(None)
                    try:
                        partial_unexpected_counts.append(e['result']['partial_unexpected_counts'])
                    except:
                        partial_unexpected_counts.append(None)
                    try:
                        partial_unexpected_index_list.append(e['result']['partial_unexpected_index_list'])
                    except:
                        partial_unexpected_index_list.append(None)
                    try:
                        partial_unexpected_list.append(e['result']['partial_unexpected_list'])
                    except:
                        partial_unexpected_list.append(None)
                    try:
                        unexpected_count.append(e['result']['unexpected_count'])
                    except:
                        unexpected_count.append(None)
                    try:
                        unexpected_percent.append(e['result']['unexpected_percent'])
                    except:
                        unexpected_percent.append(None)
                    try:
                        unexpected_percent_nonmissing.append(e['result']['unexpected_percent_nonmissing'])
                    except:
                        unexpected_percent_nonmissing.append(None)
                    try:
                        unexpected_percent_total.append(e['result']['unexpected_percent_total'])
                    except:
                        unexpected_percent_total.append(None)
                        
                    
    
    df_expectations = pd.DataFrame() 

    df_expectations['column'] = column
    df_expectations['expectation_type']=expectation_type
    df_expectations['element_count'] = element_count
    df_expectations['missing_count'] = missing_count
    df_expectations['missing_percent'] = missing_percent
    df_expectations['unexpected_count'] = unexpected_count
    df_expectations['unexpected_percent'] = unexpected_percent
    df_expectations['unexpected_percent_nonmissing'] = unexpected_percent_nonmissing
    df_expectations['unexpected_percent_total'] = unexpected_percent_total
    df_expectations['dataframe_type']=dataframe_type
    df_expectations['timestamp_run_quality']=timestamp_run
    df_expectations['scraping_date']= pd.to_datetime(df_expectations['dataframe_type'].str[13:], format='%Y%m%d').dt.strftime('%Y-%m-%d')

    df_expectations = df_expectations[['scraping_date'] + ['dataframe_type'] + ['timestamp_run_quality']+ [ col for col in df_expectations.columns if (col != 'dataframe_type')|(col != 'timestamp_run_quality')] ]
    return df_expectations.drop_duplicates().reset_index(drop=True)