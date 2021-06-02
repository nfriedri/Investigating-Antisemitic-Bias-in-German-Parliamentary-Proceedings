"""Contains all relevant Target and Attribute sets for the defined bias specifications"""

"""ANTI_SEMITISM Target Sets"""

JEWISH_RT = [
    "jude", "juedisch", "judentum", "orthodox", "israel", "mosaisch", "israelitisch", "israelit", "rothschild",
    "talmud", "synagoge", "abraham", "rabbiner", "zionistisch"]

JEWISH_BRD = [
    "judentum", "jude", "juedisch", "israel", "israelisch", "synagoge", "koscher", "orthodox", "rabbiner", "zentralrat"]

CHRISTIAN_RT = [
    "christ", "christlich", "christentum", "katholizismus", "katholisch", "evangelisch", "evangelium",
    "auferstehung", "kirche", "jesus", "taufe", "pfarrer", "bibel", "ostern"]

CHRISTIAN_BRD = [
    "christ", "christlich", "christentum", "evangelisch", "evangelium", "jesus", "katholisch", "kirche", "pfarrer",
    "taufe", "abendland"]

PROTESTANT_BRD = [
    "protestant", "protestantisch", "evangelisch", "evangelium", "landeskirche", "kirchentag", "ekd", "landesbischof",
    "lutherisch", "diakonie"]

PROTESTANT_RT = [
    "protestant", "protestantisch", "protestantismus", "evangelisch", "evangelium", "landeskirche",
    "lutherisch", "evangelisch-lutherisch", "oberkirchenrat", "reformiert"]

CATHOLIC_BRD = [
    "katholisch", "katholik", "papst", "roemisch-katholisch", "enzyklika", "paepstlich", "bischofskonferenz",
    "dioezese", "franziskus", "kurie"]

CATHOLIC_RT = [
    "katholizismus", "katholisch", "katholik", "papst", "jesuiten", "ultramontanismus", "ultramontanen",
    "jesuitenorden", "roemisch-katholisch", "zentrumspartei"]

"""ANTI-COMMUNISM Target Sets"""

CONSERVATISM_BRD = [
    "konservatismus", "tradition", "geschichte", "werte", "moral", "hierarchie", "identitaet",
    "kontinuitaet", "sicherheit", "autoritaet", "legitimitaet", "ordnung", "erhaltung", "braeuche",
    "sitten", "bewahrung", "buerger", "buergertum", "regierung", "wertordnung", "buergerlichkeit",
    "stabilitaet", "wohlstand"]

CONSERVATISM_RT = [
    "konservatismus", "tradition", "geschichte", "christentum", "adel", "monarchie", "mittelalter",
    "staende", "werte", "moral", "koenig", "kaiser", "hierarchie", "identitaet", "kontinuitaet",
    "sicherheit", "grundbesitz", "autoritaet", "legitimitaet", "ordnung", "religion", "kirche",
    "erhaltung", "treue", "tugend", "braeuche", "sitten", "bewahrung", "gottesgnadentum",
    "staendeordnung", "restauration"]

COMMUNISM_BRD = [
    "kommunismus", "proletariat", "klassengesellschaft", "revolution", "kapital", "verstaatlichung",
    "marx", "engels", "vergesellschaftung", "gemeineigentum", "widerstand", "kollektivierung", "lenin",
    "planwirtschaft", "klassenkampf", "proletariat", "revolution", "produktionsmittel", "diktatur",
    "bolschewiki", "oktoberrevolution", "raete", "sowjetunion"]

COMMUNISM_RT = [
    "sozialismus", "kommunismus", "proletariat", "arbeiter", "klassengesellschaft", "klasse", "revolution",
    "aufklaerung", "gemeinschaft", "gerechtigkeit", "armut", "kapital", "gleichheit", "chancen", "freiheit",
    "arbeiterklasse", "solidaritaet", "partei", "verstaatlichung", "gewerkschaft", "marx", "engels",
    "vergesellschaftung", "gemeineigentum", "widerstand", "kollektivierung", "arbeiterbewegung", "aufstand"]


""" Defining domains for antisemitism """
# Attribute sets defining different attribute dimensions

def antisemitic_streams(domain: str, kind: str):
    """
    Create bipolar antisemitic stream of specified domain

    Parameters
    ----------

    domain: Semantic domain to be created
      kind: whether to process a collection of Reichstag or BRD protocols
    """

    if domain == 'sentiment':
        pro = 'streicheln, Freiheit, Gesundheit, Liebe, Frieden, Freude, Freund, Himmel, loyal, Vergnuegen, Diamant, sanft, ehrlich, gluecklich, Regenbogen, Diplom, Geschenk, Ehre, Wunder, Sonnenaufgang, Familie, Lachen, Paradies, Ferien'.lower().split(
            ', ')

        con = 'Missbrauch, Absturz, Schmutz, Mord, Krankheit, Tod, Trauer, vergiften, stinken, Angriff, Katastrophe, Hass, verschmutzen, Tragoedie, Scheidung, Gefaengnis, Armut, haesslich, Krebs, toeten, faul, erbrechen, Qual'.lower().split(
            ', ')

    # nationalism/patriotism
    if domain == 'patriotism':
        if kind == 'RT':
            pro = 'patriotisch, germanisch, vaterlaendisch, deutschnational, reichstreu, vaterlandsliebe, nationalgesinnt, nationalstolz, koenigstreu, volksgeist, nationalbewusstsein, volksbewusstsein, staatstreu, nationalgefuehl'.split(
                ', ')
            con = 'unpatriotisch, undeutsch, vaterlandslos, antideutsch, dissident, landesverraeter, reichsfeindlich, reichsfeind, deutschfeindlich, fremd, fremdlaendisch, nichtdeutsch, staatsfeindlich, heimatlos'.split(
                ', ')

        elif kind == 'BRD':
            pro = 'patriotisch, vaterlandsliebe, germanisch, nationalbewusstsein, vaterlaendisch, nationalgefuehl, volkstum, patriotismus, patriot, staatstreu'.split(
                ', ')

            con = 'nichtdeutsch, vaterlandslos, landesverraeter, antideutsch, heimatlos, separatistisch, staatsfeindlich, fremd, staatenlos, dissident'.split(
                ', ')

        # economic
    elif domain == 'economic':
        pro = 'geben, großzuegigkeit, großzuegig, selbstlos, genuegsam, großmut, uneigennuetzig, sparsam, proletariat, armut, industriearbeiter'.split(
            ', ')

        con = 'nehmen, gier, gierig, egoistisch, habgierig, habsucht, eigennuetzig, verschwenderisch, bourgeoisie, wohlstand, bankier, wucher'.split(
            ', ')

    # conspiracy
    elif domain == 'conspiratorial':
        pro = 'loyal, kamerad, ehrlichkeit, ersichtlich, aufrichtig, vertrauenswuerdig, wahr, ehrlich, unschuldig, freundschaftlich, hell, zugaenglich, machtlos, ohnmacht, untertan'.split(
            ', ')

        con = 'illoyal, spitzel, verrat, geheim, betruegerisch, hinterlistig, unwahr, zweifelhaft, verbrecher, bedrohlich, dunkel, geheimnis, einflussreich, weltmacht, herrschaft, verschwoerung'.split(
            ', ')

    # ethics
    elif domain == 'ethic':
        pro = 'bescheiden, sittlich, anstaendig, tugendhaft, charakterfest, wuerdig, treu, moralisch, ehrlich, gesittet, gewissenhaft, vorbildlich'.split(
            ', ')
        con = 'unbescheiden, unsittlich, unanstaendig, luestern, korrupt, unwuerdig, untreu, unmoralisch, unehrlich, verdorben, gewissenlos, barbarisch'.split(
            ', ')

    # religion
    elif domain == 'religious':
        pro = 'glaeubige, geistlich, engel, heilig, fromm, geheiligt, goettlich, ehrwuerdig, treu, glaeubig, religioes'.split(
            ', ')

        con = 'atheist, weltlich, teufel, irdisch, atheistisch, heidnisch, gottlos, verflucht, untreu, unglaeubig, irreligioes, gotteslaesterung'.split(
            ', ')

    # racism
    elif domain == 'racist':
        pro = 'normal, ueberlegenheit, gleichheit, angenehm, freundlich, ehrenwert, sympathie, akzeptiert, besser, national, rein, ueberlegen, sauber, ehrenhaft'.split(
            ', ')
        con = 'seltsam, unterlegenheit, ungleichheit, unangenehm, boshaft, schaendlich, hass, abgelehnt, schlechter, fremdlaendisch, unrein, unterlegen, schmutzig, verseucht, schaedlich, niedertraechtig'.split(
            ', ')

    return pro, con


""" Defining domains for anti-communism """

def anticommunism_streams(domain: str, kind: str):
    arg1 = []
    arg2 = []

    # sentiments
    if domain == 'sentiment':
        arg1 = ["streicheln", "freiheit", "gesundheit", "liebe", "frieden", "freude", "freund", "himmel", "loyal",
                "vergnuegen", "diamant", "sanft", "ehrlich", "gluecklich", "regenbogen", "geschenk", "ehre", "wunder",
                "sonnenaufgang", "familie", "lachen", "paradies", "ferien"]
        arg2 = ["missbrauch", "absturz", "schmutz", "mord", "krankheit", "tod", "trauer", "vergiften", "stinken",
                "angriff", "katastrophe", "hass", "verschmutzen", "tragoedie", "scheidung", "gefaengnis", "armut",
                "haesslich", "krebs", "toeten", "faul", "erbrechen", "qual"]

    # politics
    if domain == 'political':
        if kind == 'BRD':
            arg1 = ["sozial", "progressiv", "gemeinschaftlich", "gemeinsam", "zivilisiert", "bewaehrt", "wirksam",
                    "etabliert", "demokratisch", "hoch", "moeglich", "fortschrittlich", "gemaessigt", "machbar",
                    "realistisch", "frueh", "kontinuierlich", "legitim", "verlaesslich", "aufrichtig", "intellektuell",
                    "sicher", "sicherheit", "fortschritt", "pragmatisch", "vertrauen", "wandel", "sachlich", "gewinn",
                    "faehig"]
            arg2 = ["unsozial", "radikal", "extrem", "gefaehrlich", "gefaehrdend", "niedrig", "nieder", "unmoeglich",
                    "undemokratisch", "unrealistisch", "spaet", "unlegitim", "gefahr", "unehrlich", "unaufrichtig",
                    "unintellektuell", "unsicher", "schwer", "schwierig", "misstrauen", "stillstand", "skandal",
                    "skandaloes", "zukunft", "unsachlich", "verlust", "unfaehig"]
        elif kind == 'RT':
            arg1 = ["sozial", "progressiv", "gemeinschaftlich", "gemeinsam", "zivilisiert", "bewaehrt", "wirksam",
                    "etabliert", "demokratisch", "hoch", "moeglich", "fortschrittlich", "gemaessigt", "machbar",
                    "realistisch", "frueh", "kontinuierlich", "legitim", "verlaesslich", "aufrichtig", "intellektuell",
                    "sicher", "sicherheit", "fortschritt", "pragmatisch", "vertrauen"]
            arg2 = ["unsozial", "radikal", "extrem", "gefaehrlich", "gefaehrdend", "niedrig", "nieder", "unmoeglich",
                    "undemokratisch", "unrealistisch", "spaet", "unlegitim", "gefahr", "unehrlich", "unaufrichtig",
                    "unintellektuell", "unsicher", "schwer", "schwierig", "misstrauen"]

    # propaganda
    if domain == 'propaganda':
        if kind == 'BRD':
            arg1 = ["ehre",
                    "ehrlich", "einsatz", "wir", "deutsch", "patriotisch", "volk", "wahrheit", "wahr", "aufrichtig",
                    "gemeinschaftlich", "wertegemeinschaft", "mitte", "frieden", "partnerschaft", "integration",
                    "wandel"]
            arg2 = ["betrueger", "betrug", "undeutsch", "unpatriotisch", "reichsfeindlich", "fremd", "kommunist",
                    "anders", "luege", "luegner", "dissident", "feind", "diktatur", "unehrlich", "feindlich",
                    "schmarotzer", "elite", "kriminelle", "kriminell"]
        elif kind == 'RT':
            arg1 = ["kamerad", "kameraden", "kameradschaft", "kameradschaftlich", "vaterland", "patriot", "ehre",
                    "ehrlich", "einsatz", "untertan", "rein", "wir", "heimat", "deutsch", "deutschland", "truppe",
                    "nationalstolz", "patriotisch", "volk", "befreiung", "front", "wahrheit", "wahr"]
            arg2 = ["sabotage", "saboteur", "betrueger", "betrug", "gauner", "schwindel", "schwindler", "parasit",
                    "volksfeind", "reichsfeind", "undeutsch", "unpatriotisch", "reichsfeindlich", "volksverraeter",
                    "spion", "bolschewist", "fremd", "unrein", "kommunist", "spitzel", "anders", "luege",
                    "luegner", "dissident", "feind", "diktatur", "verschwoerung", "verschwoererisch"]

    return arg1, arg2
