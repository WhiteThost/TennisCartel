import pandas as pd
import extra_functions as ef
from extra_data import excel_path

#Gera a página Resultados

def resultados():
    f = open('resultados.html','w')
    df = pd.read_excel(io = excel_path, sheet_name = f"ATP - Torneios")
    atp = ef.dic_torneios(ef.dataframe_to_list(df), "atp")
    df = pd.read_excel(io = excel_path, sheet_name = f"WTA - Torneios")
    wta = ef.dic_torneios(ef.dataframe_to_list(df), "wta")

    lista = ""
    for e in ("A decorrer", "Terminado"):
        for comp in (atp, wta):
            if len(comp) != 0:
                for t in dict.keys(comp):
                    if comp[t]['estado'] == e:
                        lista += ef.torneio_html(comp[t])



    lista_html = f"""
            <div>
            <ul class="torneios">
            {lista}
            </ul>
            </div>
            """

    full_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>Resultados</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css/main.css">
    </head>
    <body>
        <div id="nav-placeholder"></div>
            <script>$(function(){{$("#nav-placeholder").load("nav.html");}});</script>
            <div class="big-logo">
            <div class="container">
                <h1 class="titulo">Result<span>ados</span></h1>
            </div>        
        </div>
        {lista_html}
    </body>
    """

    f.write(full_html)
    f.close()

    print(f'Resultados: atualizado')

resultados()
