import os
import tkinter
import tkinter.messagebox
import customtkinter
import subprocess
import shutil


def set_audio_file(entry_file):
    path = customtkinter.filedialog.askopenfilename(filetypes=[("Audio files", "*.wav *.mp3 *.flac *.ogg *.wma *.acc *.webm *.opus")])
    if not path:
        tkinter.messagebox.showerror("Error", "Please select an audio file")
        return
    elif not path.endswith(".wav"):
        tkinter.messagebox.showinfo("Info", "This file will be converted to wav format")
        convert = ["%s/tools/vgmstream-cli.exe" % os.getcwd(), "-l", "1", "-f", "0", "-L", "-o", "temp/convert.wav", "%s" % (path)]
        subprocess.check_output(convert).decode("utf-8").strip()
        file = "%s/temp/convert.wav" % os.getcwd()
        tkinter.messagebox.showinfo("Info", "Audio file converted successfully")
    entry_file.delete(0, tkinter.END)
    if os.path.isfile(file):
        entry_file.insert(0, file)
    else:
        entry_file.insert(0, path)


def convert_audio_file(audio_file):
    if audio_file.get():
        cmd = ["%s/tools/vgaudio.exe" % os.getcwd(), "--little-endian", "%s" % (audio_file.get()), "%s/converted/%s" % (os.getcwd(), music_value(combobox))]
        subprocess.check_output(cmd).decode("utf-8").strip()
        tkinter.messagebox.showinfo("Info", "Audio file converted successfully")
    else:
        tkinter.messagebox.showerror("Error", "Please select an audio file")


def music_value(combobox):
    # recuperer tout les fichiers audio du jeu qui sont dans audio_value.txt

    if combobox.get() == "Ecran de selection de fichier de sauvegarde":
        return "03_NameInput.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Première maison (Maison de Tarkin)":
        return "04_House_First.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Fanfare d'obtention d'item":
        return "05_BigItemGetFanfare.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Field First (?)":
        return "06_Field_First.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "(?)":
        return "07_Owl.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "(?)":
        return "07_OwlLast.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Fanfare Epée":
        return "08_Fanfare_Sword.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Field Normal Intro (?)":
        return "09_Field_Normal_Intro.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Field Normal (?)":
        return "10_Field_Normal.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Meve (?)":
        return "11_Meve.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Forêt étrange":
        return "12_StrangeForest.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Intro boost (Nuts)":
        return "13_Nuts_intro.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Boost (Nuts)":
        return "14_Nuts.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Shop":
        return "15_Shop.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Shop Rapide":
        return "15_Shop_Fast.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Fée":
        return "16_Fairy.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Ouverture grotte":
        return "17_NazoTokiSeikaiOn.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Shop du jeu":
        return "18_GameShop.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Maison (?)":
        return "19_House.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Chanson de Marine":
        return "20_MarineSing.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Obtention d'item":
        return "21_ItemGetFanfare.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Caverne":
        return "22_Cave.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon 1 (Tail Cave)":
        return "23_Dangeon1_TailCave.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon 2 (2D Cave)":
        return "24_Dangeon_2DCave.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon Boss Middle":
        return "25_Dangeon_BossMiddle.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon Boss":
        return "26_Dangeon_Boss.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Fanfare d'obtention d'instrument":
        return "28_Fanfare_InstrumentsGet.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Violon":
        return "29_Inst_Violin.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Event Sauvetage de Bowwow":
        return "30_Event_RescueBowwow.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Event Sauvetage de Bowwow Intro":
        return "31_Event_RescueBowwow_intro.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Wright":
        return "32_Wright.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon 2 (Pot Cave)":
        return "34_Dangeon2_PotCave.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Cor":
        return "35_Inst_Horn.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Richard":
        return "36_Richard.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Event Singe":
        return "37_Event_Monkey.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon Chateau":
        return "38_Dangeon_Castle.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon Clé":
        return "39_Dangeon_Key.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Cloche":
        return "40_Inst_Bell.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Event Abeille":
        return "41_Event_Bee.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Village des animaux":
        return "42_AnimalVillage.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Maison de la chèvre":
        return "43_GoatHouse.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Entrée du rêve":
        return "44_DreamShrine_Entrance.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Lit du rêve":
        return "45_DreamShrine_BedIn.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Rêve":
        return "46_DreamShrine.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Event Marine sur la plage":
        return "47_Event_MarineInBeach.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Event Rendez-vous avec Marine":
        return "48_Event_DateWithMarine.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Ocarina Poisson du vent":
        return "49_Ocarina_FishOfWind.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "TaruTaru":
        return "50_TaruTaru.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "TaruTaru Après le sauvetage":
        return "50_TaruTaru_AfterRescue.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Event Pêcheur ouvert":
        return "51_Event_BasinAnglerOpen.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon 4 (Pêcheur)":
        return "52_Dangeon4_BasinAngler.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Harpe":
        return "53_Inst_Harp.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Ocarina Manbo de Manbow":
        return "54_Ocarina_ManboOfManbow.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Maison hantée":
        return "55_GhostHouse.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Pêcheur":
        return "56_FishingMan.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon 5 (Poisson-chat)":
        return "57_Dangeon5_CatFish.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Défaite":
        return "58_DefeatLoop.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Marimba":
        return "59_Inst_Marimba.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Ocarina Âme de grenouille":
        return "60_Ocarina_SoulOfFrog.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon 6 (Temple du visage)":
        return "62_Dangeon6_TempleOfFace.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Triangle":
        return "63_Inst_Triangle.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon Vêtements":
        return "64_Dangeon_Clothes.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Résurrection du poulet":
        return "65_ResuscitationOfChiken.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Maison du poulet":
        return "66_ChikenHut.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon 7 (Tour de l'aigle)":
        return "67_Dangeon7_TowerOfEagle.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon 7 (Boss event)":
        return "69_Dangeon7_Boss_event.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Orgue":
        return "70_Inst_Organ.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon 7 (Entrée de la bataille)":
        return "71_Dangeon7_EntranceBattle.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon 7 (Rocher de la tortue)":
        return "72_Dangeon7_TurtleRock.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Tambour":
        return "73_Inst_Drum.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Rapides (Jeu de radeau)":
        return "74_RapidsFallGameOfRaft.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Donjon Oeuf sacré":
        return "76_Dangeon_HolyEgg.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Dernier boss (Texte de démo)":
        return "77_LastBoss_DemoText.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Dernier boss (Apparition-Bataille)":
        return "78_LastBoss_Appear-Battle.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Dernier boss (Victoire)":
        return "79_LastBossWin.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Démonstration après le dernier boss":
        return "80_Demo_AfterLastBoss.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Démonstration après le dernier boss (Plus de piste)":
        return "80_Demo_AfterLastBossPlusTrack.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Fin":
        return "82_Ending.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Game Over":
        return "83_GameOver.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Titre (Pas d'intro)":
        return "84_Title_NoIntro.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Chanson de Totakeke":
        return "85_TotakekeSong.ry.48.dspadpcm.bfstm"
    elif combobox.get() == "Nom de Zelda":
        return "86_ZeldaName.ry.48.dspadpcm.bfstm"



def audio_copy_file():
    roaming_folder = os.getenv('appdata')
    game_mods_folder = "01006BB00C6F0000/Custom Audio/romfs/region_common/audio/stream"
    yuzu_folder_mods = "%s/yuzu/load/%s" % (roaming_folder, game_mods_folder)
    ryujinx_folder = "%s/Ryujinx/mods/contents/%s" % (roaming_folder, game_mods_folder)
    for file in os.listdir("converted"):
        if Emulator.get() == "Yuzu":
            if not os.path.exists(yuzu_folder_mods):
                os.makedirs(yuzu_folder_mods)
            shutil.copyfile("%s/converted/%s" % (os.getcwd(), file), "%s/yuzu/load/%s/%s" % (roaming_folder, game_mods_folder, file))
        if Emulator.get() == "Ryujinx":
            if not os.path.exists(ryujinx_folder):
                os.makedirs(ryujinx_folder)
            shutil.copyfile("%s/converted/%s" % (os.getcwd(), file), "%s/Ryujinx/mods/contents/%s/%s" % (roaming_folder, game_mods_folder, file))
        if Emulator.get() == "Console":
            if not os.path.exists("%s/Console/%s" % (os.getcwd(), game_mods_folder)):
                os.makedirs("%s/Console/%s" % (os.getcwd(), game_mods_folder))
            shutil.copyfile("%s/converted/%s" % (os.getcwd(), file), "%s/Console/%s/%s" % (os.getcwd(), game_mods_folder, file))
    tkinter.messagebox.showinfo("Info", "Audio file copied successfully")


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()

combobox = customtkinter.CTkComboBox(app, values=[' Ecran de selection de fichier de sauvegarde', ' Première maison (Maison de Tarkin)', " Fanfare d'obtention d'item", ' Field First (?)', ' (?)', ' (?)', ' Fanfare Epée', ' Field Normal Intro (?)', ' Field Normal (?)', ' Meve (?)', ' Forêt étrange', ' Intro boost (Nuts)', ' Boost (Nuts)', ' Shop', ' Shop Rapide', ' Fée', ' Ouverture grotte', ' Shop du jeu', ' Maison (?)', ' Chanson de Marine', " Obtention d'item", ' Caverne', ' Donjon 1 (Tail Cave)', ' Donjon 2 (2D Cave)', ' Donjon Boss Middle', ' Donjon Boss', " Fanfare d'obtention d'instrument", ' Violon', ' Event Sauvetage de Bowwow', ' Event Sauvetage de Bowwow Intro', ' Wright', ' Donjon 2 (Pot Cave)', ' Cor', ' Richard', ' Event Singe', ' Donjon Chateau', ' Donjon Clé', ' Cloche', ' Event Abeille', ' Village des animaux', ' Maison de la chèvre', ' Entrée du rêve', ' Lit du rêve', ' Rêve', ' Event Marine sur la plage', ' Event Rendez-vous avec Marine', ' Ocarina Poisson du vent', ' TaruTaru', ' TaruTaru Après le sauvetage', ' Event Pêcheur ouvert', ' Donjon 4 (Pêcheur)', ' Harpe', ' Ocarina Manbo de Manbow', ' Maison hantée', ' Pêcheur', ' Donjon 5 (Poisson-chat)', ' Défaite', ' Marimba', ' Ocarina Âme de grenouille', ' Donjon 6 (Temple du visage)', ' Triangle', ' Donjon Vêtements', ' Résurrection du poulet', ' Maison du poulet', " Donjon 7 (Tour de l'aigle)", ' Donjon 7 (Boss event)', ' Orgue', ' Donjon 7 (Entrée de la bataille)', ' Donjon 7 (Rocher de la tortue)', ' Tambour', ' Rapides (Jeu de radeau)', ' Donjon Oeuf sacré', ' Dernier boss (Texte de démo)', ' Dernier boss (Apparition-Bataille)', ' Dernier boss (Victoire)', ' Démonstration après le dernier boss', ' Démonstration après le dernier boss (Plus de piste)', ' Fin', ' Game Over', " Titre (Pas d'intro)", ' Chanson de Totakeke', ' Nom de Zelda'])
combobox.place(x=50, y=50)

audio_path = customtkinter.CTkEntry(app)
audio_path.place(x=50, y=130)
button = customtkinter.CTkButton(app, text="Custom Audio", command=lambda: set_audio_file(audio_path))
button.place(x=50, y=90)

convert_button = customtkinter.CTkButton(app, text="Convert Audio", command=lambda: convert_audio_file(audio_path))
convert_button.place(x=50, y=170)

copy_audio = customtkinter.CTkButton(app, text="Copy Audio", command=lambda: audio_copy_file())
copy_audio.place(x=50, y=210)

Emulator = customtkinter.CTkComboBox(app, values=["Yuzu", "Ryujinx", "Console"])
Emulator.place(x=50, y=10)

About = customtkinter.CTkLabel(app, text="Custom Sound for LAS\nVersion 0.1.0\nDeveloped by: Zekann & Nymfya", font=("Arial", 12))
About.place(x=57, y=250)

app.geometry("250x300")
app.title("Custom Sound for LAS")
app.resizable(False, False)
app.iconbitmap("%s/icon.ico" % os.getcwd())

app.mainloop()
