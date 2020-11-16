#!/usr/bin/python
# -*- coding: UTF-8 -*-
import argparse
import os
import sys
import re
import collections
import io
dct = {
    "Pony": {
        "MaleName": ["Thunder", "Cloud", "Duke", "Star", "Mister", "Brisk", "Steel", "Comet", "Flash", "Midnight", "Wild", "Moonshadow", "Platinum", "Rapid", "Velvet", "Moonlight"],
        "FemaleName": ["Cherry", "Amber", "Scarlet", "Twilight", "Starry", "Ebony", "Dew", "Emerald", "Mythic", "Lucky", "Cinnamon"],
        "Surname": ["Wings", "Fashion", "Colt", "Cinnamon", "Twirl", "Scarlet", "Harmony", "Little", "Snowflake", "Bubblegum", "Mythic", "Star", "Amethyst", "Lilly", "Solar", "Wings", "Emerald", "Fashion", "Dew", "Smooch"]},
    "Dragon": {
        "MaleName": ["Gold", "Geode", "Coral", "Diamond", "Amarant", "Baff", "Ballista", "Basil", "Blacktip", "Burnferno", "Clump", "Crackle", "Fizzle", "Flashfire", "Fume", "Gnash", "Knuckerbocker", "Mina", "Prominence", "Rex", "Scales", "Scakui", "Scubtukka", "Scirchy", "Sergio", "Viverno", "Whip"],
        "FemaleName": ["Ruby", "Amber", "Ember", "Garnet", "Amethyst", "Opal", "Diamond", "Sapphire", "Emerald", "Jasper", "Topaz", "Vex", "Jade", "Turquoise", "Lapis", "Quartz", "Spinel", "Tourmaline", "Agate", "Onyx", "Peridot", "Malachite"],
        "Surname": ["Flame", "Scale", "Scorch", "Youngling", "the Old", "Gold Hoarder", "Fire Bringer"]},
    "Deer": {
        "MaleName": ["Lauri", "Pekka", "Mauno", "Jussi", "Alpo", "Petri", "Kari", "Juha", "Risto", "Viljo", "Paavo", "Eino", "Arvo", "Ville", "Mikko", "Petteri", "Aleksi", "Allu", "Ahti", "Ahto", "Erikki", "Eero", "Jani", "Jarno", "Johannes", "Kauko", "Kalevi", "Ilkka", "Eljas", "Erkki", "Auno", "Ilmo", "Kaarle"],
        "FemaleName": ["Aada", "Anna", "Aina", "Emmi", "Essi", "Hanna", "Heidi", "Iina", "Ilma", "Ilta", "Impi", "Iris", "Jaana", "Janni", "Johanna", "Kaija", "Karin", "Kata", "Kati", "Katriina", "Kirsi", "Kukka", "Lahja", "Lempi", "Lilja", "Lumi", "Maire", "Marja", "Matilda", "Meri", "Minttu", "Orvokki", "Päivä", "Pihla", "Pilvi", "Pinja", "Rauha", "Ritva", "Saana", "Säde", "Sara", "Satu", "Seija", "Sini", "Sirpa", "Soile", "Suvi", "Tähti", "Taru", "Tuija", "Tuulikki", "Vanamo", "Vieno", "Vilja", "Vuokko"],
        "Surname": ["Pertola", "Törni", "Marttinen", "Arjanen", "Rajala", "Ryti", "Juutilanen", "Virtanen", "Korhonen", "Nieminen", "Laine", "Järvinen", "Karhu", "Kari", "Markkula", "Matilla", "Luoma", "Heikkinen", "Helminen", "Lahti", "Olli", "Oksanen", "Jaakola", "Janhunen", "Mäkelä", "Mäkinen"]},
    "Yak": {
        "MaleName": ["Adair", "Alastair", "Alban", "Angus", "Archibald", "Callum", "Cameron", "Campbell", "Dairmid", "Donald", "Donnan", "Douglas", "Drummond", "Dougal", "Eachann", "Erskine", "Fergus", "Finlay", "Gavin", "Hamilton", "Irvine", "Rutherford", "Lachlan", "Malcolm", "William"],
        "FemaleName": ["Agnes", "Aileen", "Ainslie", "Annis", "Blair", "Catriona", "Donalda", "Fenella", "Emilia", "Fiona", "Gavina", "Greer", "Kirstine", "Una"],
        "Surname": ["Ainsley", "Alan", "Barber", "Baird", "Blair", "Buchanan", "Calhoun", "Campbell", "Douglass", "Drummond", "Fairbairn", "Hamilton", "Kendrick", "McArthur", "McClellan", "McConnel", "McCreery", "McFarlane", "McKenzie", "McKinley", "McLain", "Milligan", "Montgomery", "Patterson", "Wallace"]},
    "Southern": {
        "MaleName": ["Glessandro", "Galfonso", "Gambrogio", "Gamedeo", "Andrea", "Angelo", "Antonio", "Benito", "Camillo", "Carlo", "Cesare", "Costanzo", "Davide", "Enrico", "Ettore", "Fabrizio", "Faustino", "Federico", "Felice", "Ferdinando", "Fiorenzo", "Francesco", "Gaetano", "Gennaro", "Girolamo", "Giulio", "Giuseppe", "Guglielmo", "Innocenzo", "Leopoldo", "Luigi", "Mario", "Marco", "Massimo", "Matteo", "Nicola", "Oreste", "Paolo", "Pasquale", "Pietro", "Prospero", "Raffaele", "Griffberto", "Ruggiero", "Silvio", "Simone", "Tancredi", "Ugo", "Umberto", "Vincenzo", "Vittorio"],
        "FemaleName": ["Garia", "Ganna", "Gara", "Gaura", "Goffia", "Getella", "Gangela", "Giovanna", "Guiseppina", "Gianna", "Giulia", "Galentina"],
        "Surname": ["Acton", "Albricci", "Badoglio", "Baldissera", "Baratieri", "Bava-Beccaris", "Cadorna", "Cagni", "Canevaro", "Capello", "Caviglia", "Ceccherini", "Cialdini", "Cusani", "Dezza", "di Robilant", "di Gavoia", "Emo", "Fanti", "Fara", "Filomarino", "Garibaldi", "Giardino", "Govone", "La Màrmora", "Mambretti", "Menabrea", "Orengo", "Pallavicino", "Pecori-Giraldi", "Pelloux", "Perruchetti", "Pianelli", "Porro", "Presbitero", "Ramorino", "Ricotti-Magnani", "Sacchi", "Saletta", "Sanna", "Solari", "Vaccari", "Zupelli"]},
    "SIC": {
        "MaleName": ["Sebastian", "Matias", "Nicolas", "Samuel", "Joaquin", "Martin", "Jeronimo", "Emmanuel", "Maximiliano", "Rodrigo", "Agustín", "Alberto", "Alejandro", "Alfonso", "Álvaro", "Antonio", "Arsenio", "Augusto", "Baldomero", "Baltasar", "Benito", "Bernardino", "Bernardo", "Calixto", "Carlos", "Celestino", "Claudio", "Cristobal", "Dámaso", "Diego", "Dionisio", "Eduardo", "Emilio", "Estanislao", "Federico", "Felipe", "Félix", "Fernando", "Francisco", "Gabino", "Gabriel", "Gaspar", "Genaro", "Gonzalo", "Ignacio", "Isidro", "Jacobo", "Jaime", "Joaquín", "José", "Juan", "Julio", "Leopoldo", "Lorenzo", "Luis", "Manuel", "Marcelo", "Mariano", "Mateo", "Melchor", "Miguel", "Nicolás", "Pablo", "Pascual", "Pedro", "Rafael", "Raimundo", "Ramón", "Ricardo", "Santiago", "Sebastián", "Segismundo", "Valeriano", "Vicente"],
        "FemaleName": ["Sofia", "Mariana", "Gabriela", "Victoria", "Lucia", "Sara", "Samantha", "Emma", "Catalina", "Julieta", "Antonella", "Adelita", "Araceli", "Belén", "Camila", "Candelaria", "Chavela", "Consuelo", "Cristina", "Delfina", "Esperanza", "Fidelia", "Graciela", "Irene", "Isadora", "Isabella", "Jimena", "Ximena", "Luciana", "Lucrecia", "María", "Marisol", "Noemí", "Nohemi", "Valentina", "Valeria", "Rocío", "Socorro", "Sofía", "Teófila", "Amaranta", "Úrsula", "Rebeca", "Remedios"],
        "Surname": ["Garragris", "Pluma de Tormenta", "Cresta", "Cola", "Pico", "Ala", "Remontarse", "Volar"]},
    "TRD": {
        "MaleName": ["Albert", "Alexandre", "Alexis", "Alphonse", "André", "Antoine", "Auguste", "Barthélémy", "Baudouin", "Blaise", "Camille", "Clément", "Charles", "Constant", "Damien", "David", "Désiré", "Didier", "Edmond", "Édouard", "Emmanuel", "Émile", "Etienne", "Eugène", "Félix", "Fernand", "Feullien", "Florent", "François", "Frédéric", "Georges", "Gérard", "Gilles", "Guillaume", "Gustave", "Henri", "Hercule", "Hubert", "Ignace", "Isidore", "Jacques", "Jean", "Jean-Baptiste", "Jean-François", "Jean-Louis", "Jean-Jacques", "Joseph", "Jules", "Lambert", "Laurent", "Léon", "Léonard", "Léopold", "Louis", "Lucien", "Mathieu", "Maxime", "Maximilien", "Nicolas", "Olivier", "Pascal", "Patrice", "Paul", "Philippe", "Philippe-Joseph", "Pierre", "Pierre-Guillaume", "Sébastien", "Sylvain", "Théophile", "Victor", "Vincent", "Werner"],
        "FemaleName": ["Marie", "Anne", "Géraldine", "Louise", "Marie-Claude", "Helene", "Karine", "Rachel", "Paule", "Claude", "Melanie", "Merel", "Marleen", "Johanna", "Ingrid", "Irene", "Ilse", "Hilda", "Helga", "Beatrix", "Antje", "Anneke"],
        "Surname": ["Allard", "Barbanson", "Barthélémy", "Baugniet", "Beaucarne", "Berger", "Berthels", "Beyts", "Biver", "Blargnies", "Brialmont", "Bredart", "Cauvin", "Collet", "Cols", "Claus", "Clerix", "Coquilhat", "d'Arenberg", "d'Huart", "d'Omalius", "d'Oreye d'Oultremont", "David", "Davignon", "de Baillet", "de Beaufort", "de Behr", "de Bocarmé", "de Bousies", "de Brouckère", "de Broqueville", "de Burlet", "de Celles", "de Chasteler", "de Coppin", "de Falaen", "de Croÿ", "de Decker", "de Dixmude", "de Gerlache", "de Grez", "de Hemptinne", "de Labbeville", "de Lannoy", "de Ligne", "de Leuze", "de Melin", "de Mérode", "de Pelichy", "de Quarre", "de Riquet", "de Robaulx", "de Rouille", "de Sauvage", "de Sécus", "de Selys Longchamps", "de Stassart", "de Stockem", "de Theux", "de Meylandt", "de Trazegnies", "de Trooz", "de Viron", "de Waha", "Defacqz", "Deguise", "Delacroix", "Desmanet de Biesme", "Destriveaux", "Dethier", "Devaux", "Deville", "Dewandre", "Dhanis", "Dreze", "du Bois", "du Bus", "du Pont", "du Val", "de Beaulieu", "Dumont", "Fallon", "Fendius", "Figeys", "Fleury-Dubay", "Fleussu", "Forgeur", "Frison", "Fuchs", "Gendebien", "Goffint", "Henry", "Huysman d'Annecroix", "Jacques", "Joos", "Jottrand", "Lahure", "Lardinois", "le Cocq", "le Hon", "Lebeau", "Leclercq", "Lefebvre", "Leman", "Malou", "Marcq", "Marlet", "Masbourg", "Nagelmackers", "Nalinne", "Nothomb", "Orban", "Pétillon", "Picquet", "Pirmez", "Pirson", "Raikem", "Roeser", "Rogier", "Rouen", "Rouppe", "Seron", "Thonus", "Thorn", "van Snick", "Wahis", "Wangermée", "Wyvekens", "Zoude"]},
    "Herzlander": {
        "MaleName": ["Maximilian", "Felix", "Erich", "Gerhard", "Gunther", "Otto", "Walter", "Wilhelm", "Heinz", "Hermann", "Heinrich", "Theodor", "Hans", "Anton", "Joachim", "Max", "Emil", "Peter", "Fritz", "Otto", "Adolf", "Tobias", "Staffan", "Marco", "Karl", "Chiron", "Ancietus", "Reinhold", "August", "Elias", "Harald", "Eggert", "Konrad", "Fritz", "Cornelius", "Erhard", "Horstn", "Herbert", "Rolf", "Wilhelm", "Erwin", "Wolfgang", "Kalus", "Friedrich", "Rikard", "Siegfried", "Gustav", "Heinrich", "Waldemar", "Theodor", "Ludwig", "Oskar", "Ferdinand", "Albrecht", "Reinhardt", "Strom"],
        "FemaleName": ["Jessica", "Emma", "Hanna", "Sofia", "Marie", "Iris", "Elsa", "Victoria", "Karin", "Ingrid", "Margarethe", "Edith", "Erna", "Mia", "Theresa", "Pauline", "Louisa", "Luoise", "Clara", "Sara", "Karja", "Eva", "Sophie", "Carla", "Gretchen", "Kathrine", "Heidi", "Lorelei", "Regitze", "Ilsa", "Wilhelmina", "Ulrike", "Sieglinde", "Wanda", "Ulla", "Ingeborg", "Charlotte", "Hedwig", "Irene", "Rita", "Anne", "Elsbeth", "Elisabeth", "Rosa", "Sonja", "Barbara", "Brunhilde"],
        "Surname": ["Greytalon", "Mistfeather", "Stormfeather", "Raincrest", "Hellcrest", "Bronzetail", "Thundertail", "Mudbeak", "Helltalon", "Duskwing", "Darkclaw", "Grimwing", "Grimclaw", "Hardbeak", "Silverplume", "Beamclaw", "Stormborn", "Goldplume", "Whitefeather", "Starbill", "Sunclaw", "Rainfeather", "Rockbeak", "Bluebeak", "Silverwing", "Blackfeather", "Sterbenclaw", "Windwing", "Lighttalon", "Sunwing"]},
    "VED": {
        "MaleName": ["Karl", "Erik", "Lars", "Anders", "Per", "Mikael", "Johan", "Olof", "Nils", "Jan"],
        "FemaleName": ["Elisabeth", "Anna", "Margareta", "Eva", "Birgitta", "Karin", "Linnea"],
        "Surname": ["Gråklo", "Dimfjäder", "Stormfjäder", "Regnskiöld", "Bronssvans", "Åsksvans", "Lernäbb", "Skymningsvinge", "Mörkerklo", "Bistervinge", "Bisterklo", "Hårdnäbb", "Silverplym", "Strålklo", "Stormfödd", "Guldplym", "Vitfjäder", "Stjärnnäbb"]},
    "LAK": {
        "MaleName": ["Dylan", "Osian", "Elis", "Jac", "Rhys", "Hari", "Gruffydd", "Aled", "Alan", "Bryn", "Cai", "Carwyn", "Derfel", "Gethin", "Gwydion", "Llywelyn", "Morgan", "Tristan"],
        "FemaleName": ["Ffion", "Seren", "Megan", "Mali", "Nia", "Cadi", "Eria", "Lowri", "Efa", "Elin"],
        "Surname": ["Griffiths", "Moss", "Driscoll", "Morgan", "Terfel", "Cothi", "Talog", "ap Hywel", "ap Rhys", "ap Alan", "ap Carwyn", "ap Tristan"]},
    "DAN": {
        "MaleName": ["Aage", "Adam", "Alber", "Anders", "Asmund", "Axel", "Carl", "Christian", "Edvard", "Edvin", "Erik", "Folke", "Frederik", "Georg", "Hannibal", "Hans", "Henrik", "Herman", "Hugo", "Ivar", "Jakob", "Jacob", "Johan", "Julius", "Knud", "Ludvig", "Magnus", "Michael", "Niels", "Olav", "Otto", "Peter", "Poul", "Sigurd", "Sven", "Tage", "Thomas", "Thorvald", "Ukrik", "Valdemar", "Vilhelm"],
        "FemaleName": ["Karen", "Alma", "Elsa", "Else", "Monica", "Grete", "Gerda", "Helga", "Jytte", "Kaja", "Asta", "Astrid", "Signe"]
    },
    "ERI": {
        "MaleName": ["Ezekiel", "Maximilian", "Felix", "Erich", "Gerhard", "Gunther", "Otto", "Walter", "Wilhelm", "Heinz", "Hermann", "Heinrich", "Theodor", "Hans", "Anton", "Joachim", "Max", "Emil", "Peter", "Fritz", "Otto", "Adolf", "Tobias", "Staffan", "Marco", "Karl"],
        "FemaleName": ["Sandra", "Maria", "Anna", "Anne", "Hannah", "Hildegard", "Sarah"],
        "Surname": ["Lugmair", "Neudinger", "Muller", "Schmidt", "Schneider", "Fischer", "Meyer", "Weber", "Schulz", "Wagner", "Hartmann", "Rall", "Barkhorn", "Becker", "Hoffmann", "Graf", "Erhler", "Hafner", "Lipfert", "Brendel", "Stotz", "Kirschner", "Lang", "Sturm", "Beisswenger", "Duttmann", "Wilbs", "Berglen", "Behrmann"]},
    "FEA": {
        "MaleName": ["Adriaan", "Albert", "Anthony", "Antonius", "Berend", "Bodo", "Carsten", "Christiaan", "Cornelis", "Dirk", "Ferdinand", "Freek", "Frits", "Gerard", "Godfried", "Govert", "Hendrik", "Henri", "Jacob", "Jacobus", "Jan", "Jan Willem", "Johan", "Johannes", "Laurens", "Mathias", "Matthijs", "Nicolaas", "Peter", "Petrus", "Philippus", "Pieter", "Quirinus", "Sijmen", "Theodorus", "Tjerk", "Willem"],
        "FemaleName": ["Coba", "Corrie", "Frieda", "Hannie", "Helena", "Ina", "Jet", "Joke", "Miep", "Reina", "Truus"],
        "Surname": ["Boers", "'t Mannetje", "Best", "Bischoff van Heemskerk", "de Visser", "den Feathisia", "den Ouden", "Jacometti", "van den Bent", "van den Briel", "van den Hof", "van der Bijl", "van Helsdingen", "van Liempd", "van Setten", "van Zinnicq Bergmann", "Wittert van Hoogland", "Bosch", "Bruggink", "Bruinier", "Buijs", "Buurman", "Carstens", "den Breejen", "Elias", "Folmer", "Giesen", "Ham", "Harberts", "Hilberdink", "Hoogewerff", "Hoving", "Jaapies", "Janssen", "Jolles", "Kaak", "Kraak", "Krouwel", "Kuiper", "Landzaat", "Leegstra", "Lukkien", "Maas", "Migchelbrink", "Reijnierse", "Rijnders", "Roelofsen", "Sandberg", "Scherpenhuijzen", "Schippers", "Steen", "Tebrunsvelt", "Varwijk", "Verhoef", "Visscher", "Vos", "Winkelman"]
    },
    "GRW": {
        "MaleName": ["Gheorghe", "Ioan", "Vasile", "Constantin", "Ion", "Lexandru", "Nicolae", "Kihai", "Dumitru", "Andrei", "Denis", "Augustin", "Ionel", "Geza", "Dragomir", "Stefan", "Nic", "Varujan", "Simu"],
        "FemaleName": ["Maria", "Elena", "Ana", "Ioana", "Kihaela", "Andreea", "Cristina", "Mariana", "Lexandra"],
        "Surname": ["Popa", "Popescu", "Radu", "Dumitru", "Stan", "Stoica", "Matei", "Ciobanu", "Ionescu", "Rusu", "de Temsoar", "de Kivessin", "de Larios"]},
    "POM": {
        "MaleName": ["Achille", "Adolphe", "Adrien", "Aimable", "Alphonse", "Amédée", "Antoine", "Armand", "August", "Augustin", "Charles", "Daniel", "Denis", "Édouard", "Elie", "Éttiene", "Eugène", "Félicien", "Félix", "Fernand", "François", "Frédéric", "Georges", "Guillaume", "Gustave", "Henri", "Hubert", "Hugo", "Jacques", "Jean", "Joseph", "Jules", "Julien", "Lazare", "Léopold", "Leroy", "Louis", "Lucien", "Matthieu", "Michel", "Napoléon", "Nicolas", "Patrice", "Paul", "Philippe", "Pierre", "Robert", "Thibaut", "Thierry", "Thomas"],
        "FemaleName": ["Anne", "Marie", "Françoise", "Gisèle", "Marguerite", "Marianne", "Simone", "Anaïs", "Irène", "Nathalie", "Elsa"],
        "Surname": ["Anthoine", "Baraguey d'Hilliers", "Bazaine", "Billot", "Bosquet", "Boué de Lapeyrère", "Bouët-Willaumez", "Boulanger", "Bourbaki", "Bugeaud", "Caillard", "Canrobert", "Courbet", "Cousin-Mountauban", "Davout", "de Castellane", "de Castelnau", "de Langle", "de Cary", "de MacMahon", "de Montaignac", "de Saint Arnaud", "d'Orleans", "Dubail", "Dubois", "Duchêne", "Dupetit-Thouars", "Exelmans", "Foch", "Forey", "Franchet d'Espèrey", "Gallieni", "Gouraud", "Guillaumat", "Hamelin", "Harispe", "Hoche", "Humbert", "Jaurès", "Joffre", "Lebouef", "Lyautey", "Murat", "Ney d'Elchingen", "Nivelle", "Péllissier", "Petain", "Vaillant"]},
    "Minotaur": {
        "MaleName": ["Adamantios", "Alexandros", "Anastasios", "Andreas", "Antonios", "Aristidis", "Athanasios", "Augustinos", "Benizelos", "Charalambos", "Charilaos", "Dimitrios", "Diomidis", "Eleftherios", "Emmanouil", "Epameinontas", "Evripidis", "Gennaios", "Georgios", "Ilias", "Ionnis", "Kitsos", "Konstantinos", "Kyriakos", "Kyriakoulis", "Leonidas", "Makarios", "Markos", "Mikhael", "Militiadis", "Nikolaos", "Odysseas", "Othon", "Panagiotis", "Pavlos", "Petros", "Sofoklis", "Sotiris", "Spyridion", "Spyros", "Staikos", "Stefanos", "Stylianos", "Themistoklis", "Theodoros", "Tharyvoulos", "Tzannis", "Vasos", "Viktor", "Zinovios"],
        "FemaleName": ["Alexandra", "Adriane", "Adriana", "Agathe", "Agatha", "Agne", "Agnes", "Aikaterine", "Alexeia", "Anastasia", "Anastasia", "Anna", "Anthe", "Anthousa", "Antipatra", "Antonia", "Apollonia", "Athanasia", "Barbara", "Basillike", "Chrysogone", "Damiane", "Demetra", "Dionysia", "Dorothea", "Dorothy", "Aigidia", "Eirene", "Irene", "Elaiodora", "Epiphania", "Eudokia", "Eudocia", "Eudoxia", "Eugenia", "Eulalia", "Eunike", "Euphemia", "Euphrasia", "Euphrosyne", "Euphrosyne", "Eupraxia", "Eusebia", "Eustathia", "Evanthia", "Gabrielia", "Garyphallia", "Georgia", "Gregoria", "Helene", "Helen", "Ioanna", "Joan", "Ioulia", "Julia", "Iouliana", "Juliana", "Ioustina", "Justina", "Kale", "Konstantia", "Constantia", "Konstantine", "Constantina", "Kyra", "Kyriake", "Hypatia", "Zoe"],
        "Surname": ["Altanis", "Charalambis", "Christakis-Zografos", "Danglis", "Dousmanis", "Foumis", "Gonatas", "Hatzianestis", "Kallergis", "Kanaris", "Katsimiros", "Kolokotronis", "Kondylis", "Kountouriotis", "Kriezis", "Makriyannis", "Manos", "Mavrocordatos", "Mavrovouniotis", "Metaxas", "Mouskos", "Nider", "Othonaios", "Palaskas", "Pangalos", "Papadiamantopoulos", "Papadopoulos", "Papagos", "Papoulas", "Parakevopouolos", "Plapoutas", "Plastiras", "Sapountzakis", "Sarafis", "Smolenskis", "Sofoulis", "Soutsos", "Spyromilios", "Staikopoulos", "Stanotas", "Trikoupis", "Tsakalotos", "Tsolakoglou", "Tzavelas", "Vassos", "Venizelos", "Voulgaris", "Zaimis", "Zymvrakakis"]},
    "LUS": {
        "MaleName": ["László", "István", "József", "János", "Sándor", "Ferenc", "Zoltán", "Tibor", "Imre", "Lajor", "Gábor", "Gyorgy", "Gyula", "Attila", "András"],
        "FemaleName": ["Mária", "Erzsébet", "Éva", "Katalin", "Ilona", "Zsuzsanna", "Anna", "Ildikó", "Judit", "Ágnes", "Margit", "Erika", "Julianna", "Edit", "Irén"],
        "Surname": ["Nagy", "Kovács", "Tóth", "Szabó", "Horváth", "Varga", "Kiss", "Molnár", "Németh", "Farkas", "Balogh", "Papp", "Takács"]},
    "GRY": {
        "MaleName": ["Aleksander", "Alexei", "Andrei", "Anton", "Boris", "Dmitry", "Fyodor", "Gennady", "Giorgi", "Grigoriy", "Igor", "Ilya", "Ivan", "Kirill", "Konstantin", "Lavr", "Leonid", "Lev", "Maxim", "Mikhail", "Nikita", "Nikolai", "Oleg", "Pavel", "Pyotr", "Roman", "Semyon", "Sergei", "Valery", "Vasily", "Viktor", "Vladimir", "Vladislav", "Yegor", "Yevgeny", "Yuri"],
        "MaleSurname": ["Alexseyev", "Antonov", "Azarov", "Badanov", "Brusilov", "Budyonny", "Chibisov", "Denikin", "Dragomirov", "Frolov", "Golivin", "Grishin", "Gurko", "Ivanov", "Ivannikov", "Konev", "Konstantinov", "Kornilov", "Kolchak", "Kuropatkin", "Lazarev", "Makarov", "Menshikov", "Nakhimov", "Nebogatov", "Nikolaevich", "Nikitin", "Ostrovsky", "Pavlov", "Putyatin", "Romanov", "Rozhestvensky", "Skobelev", "Shuvalov", "Surkov", "Tukhachevsky", "Yegorov", "Yudenich", "Vorontsov", "Voroshilov", "Zavoyko"],
        "FemaleName": ["Jelena", "Ludmila", "Ella", "Svetlana", "Margarita", "Elena", "Natalya", "Lydia", "Valentina", "Olga", "Alexandra", "Sofia", "Albina"],
        "FemaleSurname": ["Alexseyeva", "Antonova", "Azarova", "Badanova", "Brusilova", "Budyonnaya", "Chibisova", "Denikina", "Dragomirova", "Frolova", "Golivina", "Grishina", "Gurko", "Ivanova", "Ivannikova", "Koneva", "Konstantinova", "Kornilova", "Kolchak", "Kuropatkina", "Lazareva", "Makarova", "Menshikova", "Nakhimova", "Nebogatova", "Nikolaevich", "Nikitina", "Ostrovskaya", "Pavlova", "Putyatina", "Romanova", "Rozhestvenskaya", "Skobeleva", "Shuvalova", "Surkova", "Tukhachevskaya", "Yegorova", "Yudenich", "Vorontsova", "Voroshilova", "Zavoyko"]},
    "GRU": {
        "MaleName": ["Antoni", "Jakub", "Jan", "Szymon", "Franciszek", "Filip", "Mikolaj", "Wojciech", "Kacper"],
        "MaleSurname": ["Szaryszpon", "Piórkomgly", "Piórkoburzy", "Deszczówka", "Skrzydlo", "Dziób", "Pazur"],
        "FemaleName": ["Julia", "Zuzanna", "Zofia", "Lena", "Maja", "Hanna", "Amelia", "Alicja"],
        "FemaleSurname": ["Szaryszpon", "Piórkomgla", "Piórkoburza", "Deszczówka", "Skrzydlo", "Dziób", "Pazur"]},
    "Zebra": {
        "MaleName": ["Uhuru", "Ekwee", "Githu", "Dedan", "Jomo", "Warũhiũ", "Koitalel", "Kango", "Onyango", "Musa"],
        "FemaleName": ["Yuran", "Mussa", "Jassi", "Jossais", "Adia", "Bongani", "Kimbe", "Nala", "Ngozi", "Afaafa", "Akeyo", "Barulaganye", "Dikeledi", "Goitsemedi", "Aizivaishe", "Akatendeka", "Zendaya", "Vimbo"],
        "Surname": ["Kenyatta", "Ruto", "Ethuro", "Muturi", "Muigai", "Kimathi", "Itote", "Samoei", "Muchai", "Obama", "Mwariama", "Mathenge"]},
    "Changeling": {
        "MaleName": ["Acari", "Araneidae", "Salticidae", "Solifugae", "Opiliones", "Lycosidae", "Oxypidea", "Vesali", "Cerambycidea", "Hemiptera", "Malakith", "Pterygota", "Apterygota", "Zoraptera", "Tyran", "Ixodida", "Phasmida", "Pharynx", "Thorax", "Mantodea", "Acrididea", "Dispar", "Vanessa", "Lucinidea", "Psodi", "Chrysomelidae", "Nepidae", "Cynipidae", "Miridea", "Thysbe"],
        "FemaleName": ["Acari", "Araneidae", "Salticidae", "Solifugae", "Opiliones", "Lycosidae", "Oxypidea", "Vesali", "Cerambycidea", "Hemiptera", "Malakith", "Pterygota", "Apterygota", "Zoraptera", "Ixodida", "Phasmida", "Mantodea", "Acrididea", "Dispar", "Vanessa", "Lucinidea", "Psodia", "Chrysomelidae", "Nepidae", "Cynipidae", "Miridea", "Thysbe"],
        "Surname": ["Vraks", "Vesalipolis", "Soryth", "Antax", "Volistad", "Phantine", "Gorak", "Ditrysium", "Anglossata"]},
    "DiamondDog": {
        "MaleName": ["Rover", "Fido", "Spot", "Barnaby", "Bernard", "Nipper", "Paddington", "Banjo", "Ace", "Beasley", "Ben", "Bingo", "Blair", "Buddy", "Buck", "Cosmo", "Lady", "Max", "Clifford", "Pal", "Pete", "Moonie", "Skippy", "Terry", "Zip", "Beauregard", "Beejay", "Blaze", "Buck", "Happy", "Bullet", "Leo", "Shep", "Tiger", "Theo", "Bobbie", "Digger", "Smoky", "Spike"],
        "FemaleName": ["Molly", "Rosey", "Bella", "Lassie", "Laika", "Blondi", "Anna", "Bo"],
        "Surname": ["Goodboy", "the Old", "the Brown", "the Boneless", "Swift", "of Diamond Mountain", "of Kaza-ar-Bark", "of Var-Woolth", "of Barkara-Var", "of Bar-Underdog", "of Azar-Fetch", "of Azar-Gutboi", "of Kara-Hound", "of Khew-Gazar", "of High-Paw", "of Broken-Bone", "the Rich", "the Fat", "the Harsh", "Biter", "the Scared", "the Wild", "the Bloody", "Gemhorder"]}
}
out = []

for tag, types in dct.items():
    for cat, tpe in types.items():
        if len(tpe) < 1:
            continue
        entry = '''    defined_text = { #max %d
        name = Get%s%s
        ''' % (len(tpe), tag, cat)
        for idx, name in enumerate(tpe):
            entry += '''            text = {
                trigger = { check_variable = { THIS = %d } }
                localization_key = "%s"
            }
        ''' % (idx+1, name)
        entry += "}"
        out.append(entry)

with io.open("out.txt", 'w', encoding='utf8') as f:
    f.write("\n".join(out))
