import pandas as pd
import extra_functions as ef
from extra_data import excel_path




def torneios_individuais():
 
    df = pd.read_excel(io = excel_path, sheet_name = f"ATP - Torneios")
    atp = ef.dic_torneios(ef.dataframe_to_list(df), "atp")
    df = pd.read_excel(io = excel_path, sheet_name = f"WTA - Torneios")
    wta = ef.dic_torneios(ef.dataframe_to_list(df), "wta")
    df = pd.read_excel(io = excel_path, sheet_name = f"Predictions")
    
    predicts = ef.dic_predicts(ef.dataframe_to_list(df))
    torneios = [['atp', atp[t]['ref'], atp[t]['nome']] for t in atp] + [['wta', wta[t]['ref'], wta[t]['nome']] for t in wta]

    for t in range(len(torneios)):
        ef.torneio_individual(torneios[t], predicts)

    print('Torneios-Individuais: atualizado')
