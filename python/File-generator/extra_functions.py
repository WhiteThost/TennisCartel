import extra_data as ed

#Ficheiro com pequenas funçoes.

def dataframe_to_list(df):
    lista = df.values.tolist()
    return lista

def dic_torneios(torneios, comp):
    t = {}
    for i in torneios:
        t[i[0]] = {"ref": i[0], "pais": i[1], "estado": i[2], "nome": i[3], "categoria": i[4], 
                   "date": i[5].strftime("%d-%m"), "surface": i[6], "draw": i[7], "comp": comp}
    return t

def dic_predicts(predictions):
    p = {}
    for i in predictions:
        p[i[0]] = {"ref": i[0], "comp": i[1].lower(), "torneio": i[2], "data": i[3], "ronda": i[4], "j1": i[5], "j2": i[6], "odd": i[7], "bet": i[8], "resultado": i[9]}
    return p

def torneio_html(t):

    txt = f"""
    <li class= "torneio">
        <a href="/torneios/{t["comp"]}/{t["ref"]}.html">
            <img src="https://flagpedia.net/data/flags/w1160/{ed.p_flag[t["pais"]]}.png" alt="{t["pais"]}">
            <p class="estado {ed.estados_dict[t['estado']]}">{t["estado"]}</p>
            <p class="torneio-name">{t["nome"]}</p>
            <div class="extra">
                <p class="categoria {t['comp']}">{t["categoria"]}</p>
                <p class="date">{t["date"]}</p>
                <p class="surface">{t["surface"]}</p>
                <p class="draw">{t["draw"]}</p>
            </div>
        </a>
    <li>
    """
    return txt

def prediction_html(p):

    txt = f"""
        <li class="prediction">
            <p class="comp {p["comp"]}">{p["comp"].upper()}</p>
            <p class="ronda">{p["ronda"]}</p>
            <p class="jogador j1">{p["j1"]}</p>
            <p class="jogador j2">{p["j2"]}</p>
            <p class="odd">@{p["odd"]}</p>
            <p class="bet">{p["bet"]}</p>
            <p class="resultado">{p["resultado"]}</p>
        </li>
        """
    return txt

def torneio_individual(torneio, predicts):

    f = open(f'/Users/tiago/Documents/Programacao/Crash Front-End/torneios/{torneio[0]}/{torneio[1]}.html','w')

    lista = ""

    for p in predicts:
        if predicts[p]['comp'] == torneio[0] and predicts[p]['torneio'] == torneio[1]:
                lista += prediction_html(predicts[p])

    if lista == "":
            txt =f"""
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>{torneio[2]}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../../css/main.css">
    </head>
    <body>
        <div id="nav-placeholder"></div>
        <script>
        $(function(){{$("#nav-placeholder").load("../../nav.html");}});
        </script>
        <div class="big-logo">
            <div class="container">
                <h1 class="titulo"><span>Prediction$ - </span>{torneio[2]} {torneio[0].upper()}</h1>
                <h3 class="subtitulo">Este torneio ainda não tem predicts</h3>
            </div>        
        </div>
        <div >

    </div>
</body>
        """
    else:
        txt =f"""
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <script src="https://code.jquery.com/jquery-1.10.2.js"></script>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <title>{torneio[2]}</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="../../css/main.css">
    </head>
    <body>
        <div id="nav-placeholder"></div>
        <script>
        $(function(){{$("#nav-placeholder").load("../../nav.html");}});
        </script>
        <div class="big-logo">
            <div class="container">
                <h1 class="titulo"><span>Prediction$ - </span>{torneio[2]} {torneio[0].upper()}</h1>
            </div>        
        </div>
        <div >
            <ul class="predictions">
            {lista}
            </ul>

    </div>
</body>
        """

    f.write(txt)
    f.close()  
