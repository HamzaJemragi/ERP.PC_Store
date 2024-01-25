import customtkinter
import sqlite3
import datetime
import random
import main_db
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from tkinter import scrolledtext as tkst
from tkinter import simpledialog


###-----------Database---------------------------------------------------------------------------------------------------------------------------------------------------


main_db.client_db()
main_db.stock_db()
main_db.facture_cash_db()
main_db.facture_versement_db()
main_db.bon_client_db()
main_db.mauvais_client_db()


###-----------GUI Paramètre----------------------------------------------------------------------------------------------------------------------------------------------


WIDTH = 1150
HEIGHT = 580

window = customtkinter.CTk()
window.title('Ordinateur store')
window.geometry(f'{WIDTH}x{HEIGHT}')
window.minsize(WIDTH, HEIGHT)

# configure grid layout (4x4)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=0)
window.grid_rowconfigure(1, weight=4)

customtkinter.set_appearance_mode('System')
customtkinter.set_default_color_theme('dark-blue')


###-----------Frames Fonctions----------------------------------------------------------------------------------------------------------------------------------------------


def client_frame():
    
    global global_frame
    Accueil.destroy_menu(global_frame)
    Stock.destroy_stock(global_frame)
    Facture.destroy_facture(global_frame)
    global_frame = Client()
    
    
def stock_frame():
    
    global global_frame
    Accueil.destroy_menu(global_frame)
    Client.destroy_client(global_frame)
    Facture.destroy_facture(global_frame)
    global_frame = Stock()
    
    
def facture_frame():
    
    global global_frame
    Accueil.destroy_menu(global_frame)
    Client.destroy_client(global_frame)
    Stock.destroy_stock(global_frame)
    global_frame = Facture()
    
    
def accueil_frame():
    
    global global_frame
    Client.destroy_client(global_frame)
    Stock.destroy_stock(global_frame)
    Facture.destroy_facture(global_frame)
    global_frame = Accueil()


###-----------Client Fonctions----------------------------------------------------------------------------------------------------------------------------------------------
    
    
def client_database(client_tree):
    
    global count
    
    # update the treeview
    for record in client_tree.get_children():
        client_tree.delete(record)
    
    client_db = sqlite3.connect('H_Client.db')
    client_cursor = client_db.cursor()
    
    client_cursor.execute('SELECT rowid, * FROM Client')
    
    records = client_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0:
            
            client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('evenrow',))
            
        else:
            
            client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('oddrow',))
            
        count += 1
        
    client_db.commit()
    client_db.close()
    
    
def vider_nouveau_client_entry():
    
    global_frame.n_prenom_entry.delete(0, END)
    global_frame.n_nom_entry.delete(0, END)
    global_frame.n_marque_entry.delete(0, END)
    global_frame.n_model_entry.delete(0, END)
    global_frame.n_type_entry.delete(0, END)
    global_frame.n_utiliser_entry.delete(0, END)
    global_frame.n_cpu_entry.delete(0, END)
    global_frame.n_stockage_entry.delete(0, END)
    global_frame.n_ram_entry.delete(0, END)
    global_frame.n_tel_entry.delete(0, END)
    global_frame.n_date_entry.delete(0, END)
    
    
def ajouter_nouveau_client():
    
    global global_frame, nv1, nv2, nv3, nv4, nv5, nv6, nv7, nv8, nv9, nv10, nv11
    
    nv1 = global_frame.n_prenom_entry.get()
    nv2 = global_frame.n_nom_entry.get()
    nv3 = global_frame.n_marque_entry.get()
    nv4 = global_frame.n_model_entry.get()
    nv5 = global_frame.n_type_entry.get()
    nv6 = global_frame.n_utiliser_entry.get()
    nv7 = global_frame.n_cpu_entry.get()
    nv8 = global_frame.n_stockage_entry.get()
    nv9 = global_frame.n_ram_entry.get()
    nv10 = global_frame.n_tel_entry.get()
    nv11 = global_frame.n_date_entry.get()
    
    if (nv1 == '' or nv2 == '' or nv5 == '' or nv6 == '' or nv7 == '' or nv9 == '' or nv10 == '' or nv11 == ''):
        
            messagebox.showinfo('Erreur', 'Vous oublier une(des) info(s)! reverifier.')
            
    else:
        
        client_db = sqlite3.connect('H_Client.db')
        client_cursor = client_db.cursor()
        
        client_cursor.execute("""INSERT INTO Client VALUES (:prenom, :nom, :marque, :model, :type, :utiliser, :cpu, :stockage, :ram, :tel, :date)""",
                            {
                                'prenom':nv1,
                                'nom':nv2,
                                'marque':nv3,
                                'model':nv4,
                                'type':nv5,
                                'utiliser':nv6,
                                'cpu':nv7,
                                'stockage':nv8,
                                'ram':nv9,
                                'tel':nv10,
                                'date':nv11
                            })
        
        client_db.commit()
        client_db.close()
        
        vider_nouveau_client_entry()
        client_database(global_frame.client_tree)
        
        
def vider_client_entry():
    
    global_frame.prenom_entry.delete(0, END)
    global_frame.nom_entry.delete(0, END)
    global_frame.marque_entry.delete(0, END)
    global_frame.model_entry.delete(0, END)
    global_frame.type_entry.delete(0, END)
    global_frame.utiliser_entry.delete(0, END)
    global_frame.cpu_entry.delete(0, END)
    global_frame.stockage_entry.delete(0, END)
    global_frame.ram_entry.delete(0, END)
    global_frame.tel_entry.delete(0, END)
    global_frame.date_entry.delete(0, END)
    
    
def select_client(event):
    
    vider_client_entry()
    
    selected = global_frame.client_tree.focus()
    values = global_frame.client_tree.item(selected, 'values')
    
    global_frame.prenom_entry.insert(0, values[1])
    global_frame.nom_entry.insert(0, values[2])
    global_frame.marque_entry.insert(0, values[3])
    global_frame.model_entry.insert(0, values[4])
    global_frame.type_entry.insert(0, values[5])
    global_frame.utiliser_entry.insert(0, values[6])
    global_frame.cpu_entry.insert(0, values[7])
    global_frame.stockage_entry.insert(0, values[8])
    global_frame.ram_entry.insert(0, values[9])
    global_frame.tel_entry.insert(0, values[10])
    global_frame.date_entry.insert(0, values[11])  
   
    
def ajouter_client():
    
    global global_frame, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11
    
    v1 = global_frame.prenom_entry.get()
    v2 = global_frame.nom_entry.get()
    v3 = global_frame.marque_entry.get()
    v4 = global_frame.model_entry.get()
    v5 = global_frame.type_entry.get()
    v6 = global_frame.utiliser_entry.get()
    v7 = global_frame.cpu_entry.get()
    v8 = global_frame.stockage_entry.get()
    v9 = global_frame.ram_entry.get()
    v10 = global_frame.tel_entry.get()
    v11 = global_frame.date_entry.get()
    
    if (v1 == '' or v2 == '' or v5 == '' or v6 == '' or v7 == '' or v9 == '' or v10 == '' or v11 == ''):
        
            messagebox.showinfo('Erreur', 'Vous oublier une(des) info(s)! reverifier.')
            
    else:
        
        client_db = sqlite3.connect('H_Client.db')
        client_cursor = client_db.cursor()
        
        client_cursor.execute("""INSERT INTO Client VALUES (:prenom, :nom, :marque, :model, :type, :utiliser, :cpu, :stockage, :ram, :tel, :date)""",
                            {
                                'prenom':global_frame.prenom_entry.get(),
                                'nom':global_frame.nom_entry.get(),
                                'marque':global_frame.marque_entry.get(),
                                'model':global_frame.model_entry.get(),
                                'type':global_frame.type_entry.get(),
                                'utiliser':global_frame.utiliser_entry.get(),
                                'cpu':global_frame.cpu_entry.get(),
                                'stockage':global_frame.stockage_entry.get(),
                                'ram':global_frame.ram_entry.get(),
                                'tel':global_frame.tel_entry.get(),
                                'date':global_frame.date_entry.get()
                            })
        
        client_db.commit()
        client_db.close()
        
        vider_client_entry()
        client_database(global_frame.client_tree)
        
        
def modifier_client():        
        
    try:
        
        sup = global_frame.client_tree.focus()
        value = global_frame.client_tree.item(sup, 'values')
            
        client_db = sqlite3.connect('H_Client.db')
        client_cursor =  client_db.cursor()
        
        client_cursor.execute("""UPDATE Client set
                            prenom = :p,
                            nom = :n,
                            marque = :ma,
                            model = :mo,
                            type = :ty,
                            utiliser = :u,
                            cpu = :c,
                            stockage = :s,
                            ram = :r,
                            tel = :te,
                            date = :d
                            WHERE rowid = :id""",
                            {'p': global_frame.prenom_entry.get(),
                            'n': global_frame.nom_entry.get(),
                            'ma': global_frame.marque_entry.get(),
                            'mo': global_frame.model_entry.get(),
                            'ty': global_frame.type_entry.get(),
                            'u': global_frame.utiliser_entry.get(),
                            'c': global_frame.cpu_entry.get(),
                            's': global_frame.stockage_entry.get(),
                            'r': global_frame.ram_entry.get(),
                            'te': global_frame.tel_entry.get(),
                            'd': global_frame.date_entry.get(),
                            'id': value[0]
                            })
        
        client_db.commit()
        client_db.close()
        
        # update the treeview
        for record in global_frame.client_tree.get_children():
            global_frame.client_tree.delete(record)
            
        vider_client_entry()
        client_database(global_frame.client_tree)
        
    except:
        
        messagebox.showinfo('ERREUR', "Tu as oublié(e) de sélectionner le rocord!!\nSélectionnez-le s'il vous plait.")


def supprimer_client(client_tree):
    
    try:
        
        sup = client_tree.focus()
        values = client_tree.item(sup, 'values')
        
        client_db = sqlite3.connect('H_Client.db')
        client_cursor =  client_db.cursor()
        
        client_cursor.execute('DELETE from Client WHERE rowid like ?', (values[0],))
        client_cursor.execute('CREATE TABLE if not exists Client(prenom, nom, marque, model, type, utiliser, cpu, stockage, ram, tel, date)')
        
        client_db.commit()
        client_db.close()
        
        vider_client_entry()
        client_database(client_tree)
        
        messagebox.showinfo('suppression info','La suppression est reussie.')
        
    except:
        
        messagebox.showinfo('ERREUR', "Tu as oublié(e) de sélectionner le rocord!!\nSélectionnez-le s'il vous plait.")
        
        
def supprimer_quelque_client(client_tree):
    
    reponse = messagebox.askyesno('WHOOOA!!!', 'Cela supprimera tout les sèlectionnés du tableau\nêtes-vous sûr?')
    
    if reponse == 1:
        
        selected = client_tree.selection()
        
        ids_pour_supprimer = []
        
        for record in selected:
            ids_pour_supprimer.append(client_tree.item(record, 'values')[0])
        
        client_db = sqlite3.connect('H_Client.db')
        client_cursor =  client_db.cursor()
        
        client_cursor.executemany('DELETE from Client WHERE rowid = ?', [(a,) for a in ids_pour_supprimer])
        client_cursor.execute('CREATE TABLE if not exists Client(prenom, nom, marque, model, type, utiliser, cpu, stockage, ram, tel, date)')
        
        client_db.commit()
        client_db.close()
        
        vider_client_entry()
        client_database(client_tree)
        
        
def supprimer_tous_client(client_tree):
    
    reponse = messagebox.askyesno('WHOOOA!!!', 'Cela supprimera tout du tableau\nêtes-vous sûr?')
    
    if reponse == 1:
        
        client_db = sqlite3.connect('H_Client.db')
        client_cursor =  client_db.cursor()
        
        client_cursor.execute('DROP TABLE Client')
        client_cursor.execute('CREATE TABLE if not exists Client(prenom, nom, marque, model, type, utiliser, cpu, stockage, ram, tel, date)')
        
        client_db.commit()
        client_db.close()
        
        vider_client_entry()
        
        # update the treeview
        for record in client_tree.get_children():
            client_tree.delete(record)


def recherche_client(client_tree):
    
    global count
    
    but = global_frame.recherche_entry.get()
    
    # update the treeview
    for record in client_tree.get_children():
        client_tree.delete(record)
    
    client_db = sqlite3.connect('H_Client.db')
    client_cursor = client_db.cursor()
    
    client_cursor.execute('SELECT rowid, * from Client WHERE rowid like ? or prenom like ? or nom like ? or marque like ? or model like ? or type like ? or utiliser like ? or cpu like ? or stockage like ? or ram like ? or tel like ? or date like ?', (but,but,but,but,but,but,but,but,but,but,but,but,))
    
    records = client_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('evenrow',))
            
        else:
            
            client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('oddrow',))
            
        count += 1
        
    client_db.commit()
    client_db.close()
    
    vider_client_entry()
    
    
def refraichir_client(client_tree):
    
    global count
    
    # update the treeview
    for record in client_tree.get_children():
        client_tree.delete(record)
    
    client_db = sqlite3.connect('H_Client.db')
    client_cursor = client_db.cursor()
    
    client_cursor.execute('SELECT rowid, * FROM Client')
    
    records = client_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('evenrow',))
            
        else:
            
            client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('oddrow',))
            
        count += 1
        
    client_db.commit()
    client_db.close()
    
    vider_client_entry()
    
    global_frame.recherche_entry.delete(0, END)
    
    
###-----------Stock Fonctions----------------------------------------------------------------------------------------------------------------------------------------------
    

def stock_database(stock_tree):
    
    global count
    
    # update the treeview
    for record in stock_tree.get_children():
        stock_tree.delete(record)
    
    stock_db = sqlite3.connect('Stock.db')
    stock_cursor = stock_db.cursor()
    
    stock_cursor.execute('SELECT * FROM Stock')
    
    records = stock_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            stock_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('evenrow',))            
        else:
            
            stock_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('oddrow',))
            
        count += 1
        
    stock_db.commit()
    stock_db.close()
    
    
def vider_stock_entry():
    
    global_frame.o_code_entry.delete(0, END)
    global_frame.o_marque_entry.delete(0, END)
    global_frame.o_model_entry.delete(0, END)
    global_frame.o_type_entry.delete(0, END)
    global_frame.o_utiliser_entry.delete(0, END)
    global_frame.o_os_entry.delete(0, END)
    global_frame.o_cpu_entry.delete(0, END)
    global_frame.o_gpu_entry.delete(0, END)
    global_frame.o_stockage_entry.delete(0, END)
    global_frame.o_ram_entry.delete(0, END)
    global_frame.o_prix_achat_entry.delete(0, END)
    global_frame.o_prix_vente_entry.delete(0, END)
    global_frame.stock_recherche_entry.delete(0, END)
    
    
def select_stock(event):
    
    vider_stock_entry()
    
    selected = global_frame.stock_tree.focus()
    values = global_frame.stock_tree.item(selected, 'values')
    
    global_frame.o_code_entry.insert(0 ,values[0])
    global_frame.o_marque_entry.insert(0, values[1])
    global_frame.o_model_entry.insert(0, values[2])
    global_frame.o_type_entry.insert(0, values[3])
    global_frame.o_utiliser_entry.insert(0, values[4])
    global_frame.o_os_entry.insert(0, values[5])
    global_frame.o_cpu_entry.insert(0, values[6])
    global_frame.o_gpu_entry.insert(0, values[7])
    global_frame.o_stockage_entry.insert(0, values[8])
    global_frame.o_ram_entry.insert(0, values[9])
    global_frame.o_prix_achat_entry.insert(0, values[10])
    global_frame.o_prix_vente_entry.insert(0, values[11])
    
    
def ajouter_stock():
    
    global global_frame 
    
    if (global_frame.o_code_entry.get()=='' or global_frame.o_marque_entry.get()=='' or global_frame.o_model_entry.get()=='' or global_frame.o_type_entry.get()=='' or global_frame.o_utiliser_entry.get()=='' or 
        global_frame.o_os_entry.get()== '' or global_frame.o_cpu_entry.get()=='' or global_frame.o_gpu_entry.get()=='' or global_frame.o_stockage_entry.get()=='' or global_frame.o_ram_entry.get()=='' or
        global_frame.o_prix_achat_entry.get()=='' or global_frame.o_prix_vente_entry.get()==''):
        
            messagebox.showinfo('Erreur', 'Vous oublier une(des) info(s)!\nreverifier.')
            
    else:
        
        stock_db = sqlite3.connect('Stock.db')
        stock_cursor = stock_db.cursor()
        
        stock_cursor.execute("""INSERT INTO Stock VALUES (:code, :marque, :model, :type, :utiliser, :os, :cpu, :gpu, :stockage, :ram, :prix_achat, :prix_vente)""",
                            {
                                'code':global_frame.o_code_entry.get(),
                                'marque':global_frame.o_marque_entry.get(),
                                'model':global_frame.o_model_entry.get(),
                                'type':global_frame.o_type_entry.get(),
                                'utiliser':global_frame.o_utiliser_entry.get(),
                                'os':global_frame.o_os_entry.get(),
                                'cpu':global_frame.o_cpu_entry.get(),
                                'gpu':global_frame.o_gpu_entry.get(),
                                'stockage':global_frame.o_stockage_entry.get(),
                                'ram':global_frame.o_ram_entry.get(),
                                'prix_achat':global_frame.o_prix_achat_entry.get(),
                                'prix_vente':global_frame.o_prix_vente_entry.get()
                            })
        
        stock_db.commit()
        stock_db.close()
        
        vider_stock_entry()
        stock_database(global_frame.stock_tree)
        
        
def modifier_stock():
    
    selected = global_frame.stock_tree.focus()
    
    global_frame.stock_tree.item(selected, text = '', values=(global_frame.o_code_entry.get(), global_frame.o_marque_entry.get(), global_frame.o_model_entry.get(), global_frame.o_type_entry.get(),
            global_frame.o_utiliser_entry.get(), global_frame.o_os_entry.get(), global_frame.o_cpu_entry.get(), global_frame.o_gpu_entry.get(), global_frame.o_stockage_entry.get(),
            global_frame.o_ram_entry.get(), global_frame.o_prix_achat_entry.get(), global_frame.o_prix_vente_entry.get(),))
        
    stock_db = sqlite3.connect('Stock.db')
    stock_cursor =  stock_db.cursor()
    
    stock_cursor.execute("""UPDATE Stock set
                        code = :co,
                        marque = :ma,
                        model = :mo,
                        type = :ty,
                        utiliser = :u,
                        os = :o,
                        cpu = :c,
                        gpu = :g,
                        stockage = :s,
                        ram = :r,
                        prix_achat = :pa,
                        prix_vente = :pv
                        WHERE code = :id""",
                        {'co': global_frame.o_code_entry.get(),
                        'ma': global_frame.o_marque_entry.get(),
                        'mo': global_frame.o_model_entry.get(),
                        'ty': global_frame.o_type_entry.get(),
                        'u': global_frame.o_utiliser_entry.get(),
                        'o': global_frame.o_os_entry.get(),
                        'c': global_frame.o_cpu_entry.get(),
                        'g': global_frame.o_gpu_entry.get(),
                        's': global_frame.o_stockage_entry.get(),
                        'r': global_frame.o_ram_entry.get(),
                        'pa': global_frame.o_prix_achat_entry.get(),
                        'pv': global_frame.o_prix_vente_entry.get(),
                        'id': global_frame.o_code_entry.get()
                        })
    
    stock_db.commit()
    stock_db.close()
    
    # update the treeview
    for record in global_frame.stock_tree.get_children():
        global_frame.stock_tree.delete(record)
        
    vider_stock_entry()
    stock_database(global_frame.stock_tree)
    
    
def supprimer_stock(stock_tree):
    
    sup = stock_tree.focus()
    value = stock_tree.item(sup, 'values')
    
    stock_db = sqlite3.connect('Stock.db')
    stock_cursor =  stock_db.cursor()
    
    stock_cursor.execute('DELETE from Stock WHERE code like ?', (value[0],))
    stock_cursor.execute('CREATE TABLE if not exists Stock(code, marque, model, type, utiliser, os, cpu, gpu, stockage, ram, prix_achat, prix_vente)')
    
    stock_db.commit()
    stock_db.close()
    
    vider_stock_entry()
    stock_database(stock_tree)
    
    messagebox.showinfo('suppression info','La suppression est reussie.')
    
    
def supprimer_quelque_stock(stock_tree):
    
    reponse = messagebox.askyesno('WHOOOA!!!', 'Cela supprimera tout les sèlectionnés du tableau\nêtes-vous sûr?')
    
    if reponse == 1:
        
        selected = stock_tree.selection()
        
        ids_pour_supprimer = []
        
        for record in selected:
            ids_pour_supprimer.append(stock_tree.item(record, 'values')[0])
        
        stock_db = sqlite3.connect('Stock.db')
        stock_cursor =  stock_db.cursor()
        
        stock_cursor.executemany('DELETE from Stock WHERE code = ?', [(a,) for a in ids_pour_supprimer])
        stock_cursor.execute('CREATE TABLE if not exists Stock(code, marque, model, type, utiliser, os, cpu, gpu, stockage, ram, prix_achat, prix_vente)')
        
        stock_db.commit()
        stock_db.close()
        
        vider_stock_entry()
        stock_database(stock_tree)
    
    
def supprimer_tous_stock(stock_tree):
    
    reponse = messagebox.askyesno('WHOOOA!!!', 'Cela supprimera tout du tableau\nêtes-vous sûr?')
    
    if reponse == 1:
        
        stock_db = sqlite3.connect('Stock.db')
        stock_cursor =  stock_db.cursor()
        
        stock_cursor.execute('DROP TABLE Stock')
        stock_cursor.execute('CREATE TABLE if not exists Stock(code, marque, model, type, utiliser, os, cpu, gpu, stockage, ram, prix_achat, prix_vente)')
        
        stock_db.commit()
        stock_db.close()
        
        vider_stock_entry()
        
        # update the treeview
        for record in stock_tree.get_children():
            stock_tree.delete(record)
        
    
def recherche_stock(stock_tree):
    
    global count
    
    but = global_frame.stock_recherche_entry.get()
    
    # update the treeview
    for record in stock_tree.get_children():
        stock_tree.delete(record)
    
    stock_db = sqlite3.connect('Stock.db')
    stock_cursor = stock_db.cursor()
    
    stock_cursor.execute('SELECT * from Stock WHERE code like ? or marque like ? or model like ? or type like ? or utiliser like ? or os like ? or cpu like ? or gpu like ? or stockage like ? or ram like ? or prix_vente like ?', (but, but, but, but, but, but, but, but, but, but, but,))
    
    records = stock_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            stock_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('evenrow',))
            
        else:
            
            stock_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('oddrow',))
            
        count += 1
        
    stock_db.commit()
    stock_db.close()
    
    vider_stock_entry()
    
    
def refraichir_stock(stock_tree):
    
    global count
    
    # update the treeview
    for record in stock_tree.get_children():
        stock_tree.delete(record)
    
    stock_db = sqlite3.connect('Stock.db')
    stock_cursor = stock_db.cursor()
    
    stock_cursor.execute('SELECT * FROM Stock')
    
    records = stock_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            stock_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('evenrow',))
            
        else:
            
            stock_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9], record[10], record[11]), tags = ('oddrow',))
            
        count += 1
        
    stock_db.commit()
    stock_db.close()
    
    vider_stock_entry()
    
    global_frame.stock_recherche_entry.delete(0, END)
    
    
###-----------Cash Fonctions----------------------------------------------------------------------------------------------------------------------------------------------
    
    
def cash_database(cash_tree):
    
    global count
    
    # update the treeview
    for record in cash_tree.get_children():
        cash_tree.delete(record)
    
    facture_cash_db = sqlite3.connect('Facture_Cash.db')
    facture_cash_cursor = facture_cash_db.cursor()
    
    facture_cash_cursor.execute('SELECT * FROM Cash')
    
    records = facture_cash_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            cash_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('evenrow',))
            
        else:
            
            cash_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('oddrow',))
            
        count += 1
        
    facture_cash_db.commit()
    facture_cash_db.close()
    
    
def vider_cash():
    
    global_frame.nFacture_entry_cash.delete(0, END)
    global_frame.recherche_cash_entry.delete(0, END)
    
    
def select_cash(event):
    
    vider_cash()
    
    selected = global_frame.payer_cash_tree.focus()
    values = global_frame.payer_cash_tree.item(selected, 'values')
    
    global_frame.nFacture_entry_cash.insert(0 ,values[0])
    val2 = values[1]
    val3 = values[2]
    val4 = values[3]
    val5 = values[4]
    val6 = values[5]
    val7 = values[6]
        
        
def supprimer_tous_cash(payer_cash_tree):

    reponse = messagebox.askyesno('WHOOOA!!!', 'Cela supprimera tout du tableau\nêtes-vous sûr?')
        
    if reponse == 1:
            
        facture_cash_db = sqlite3.connect('Facture_Cash.db')
        facture_cash_cursor = facture_cash_db.cursor()
        
        facture_cash_cursor.execute('DROP TABLE Cash')
        facture_cash_cursor.execute('CREATE TABLE if not exists Cash(numero, prenom, nom, cin, prix_vente, tel, date)')
        
        facture_cash_db.commit()
        facture_cash_db.close()
            
        vider_cash()
            
        # update the treeview
        for record in payer_cash_tree.get_children():
            payer_cash_tree.delete(record)
            
            
def rechercher_cash(payer_cash_tree):
    
    global count
    
    but = global_frame.recherche_cash_entry.get()
    
    # update the treeview
    for record in payer_cash_tree.get_children():
        payer_cash_tree.delete(record)
    
    facture_cash_db = sqlite3.connect('Facture_Cash.db')
    facture_cash_cursor = facture_cash_db.cursor()
    
    facture_cash_cursor.execute('SELECT * from Cash WHERE numero like ? or prenom like ? or nom like ? or cin like ? or tel like ? or date like ?', (but, but, but, but, but, but,))
    
    records = facture_cash_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            payer_cash_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('evenrow',))
            
        else:
            
            payer_cash_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('oddrow',))
            
        count += 1
        
    facture_cash_db.commit()
    facture_cash_db.close()
    
    vider_cash()
    
    
def refraichir_cash(payer_cash_tree):
    
    global count
    
    # update the treeview
    for record in payer_cash_tree.get_children():
        payer_cash_tree.delete(record)
    
    facture_cash_db = sqlite3.connect('Facture_Cash.db')
    facture_cash_cursor = facture_cash_db.cursor()
    
    facture_cash_cursor.execute('SELECT * from Cash')
    
    records = facture_cash_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            payer_cash_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('evenrow',))
            
        else:
            
            payer_cash_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('oddrow',))
            
        count += 1
        
    facture_cash_db.commit()
    facture_cash_db.close()
    
    vider_cash()
    
    
###-----------Versement Fonctions----------------------------------------------------------------------------------------------------------------------------------------------
    
    
def versement_database(versement_tree):
    
    global count
    
    # update the treeview
    for record in versement_tree.get_children():
        versement_tree.delete(record)
    
    facture_versement_db = sqlite3.connect('Facture_Versement.db')
    facture_versement_cursor = facture_versement_db.cursor()
    
    facture_versement_cursor.execute('SELECT * FROM Versement')
    
    records = facture_versement_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            versement_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags = ('evenrow',))
            
        else:
            
            versement_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags = ('oddrow',))
            
        count += 1
        
    facture_versement_db.commit()
    facture_versement_db.close()
    
    
def vider_versement():
    
    global_frame.nFacture_entry_versement.delete(0, END)
    global_frame.versement_recherche_entry.delete(0, END)
    global_frame.avance_entry_versement.delete(0, END)
    
    
def select_versement(event):
    
    vider_versement()
    
    selected = global_frame.payer_versements_tree.focus()
    values = global_frame.payer_versements_tree.item(selected, 'values')
    
    global_frame.nFacture_entry_versement.insert(0 ,values[0])
    
    
def calculer_avance():
    
    global global_frame
    
    selected = global_frame.payer_versements_tree.focus()
    value = global_frame.payer_versements_tree.item(selected, 'values')
    
    prix_de_vente = value[4]    
    avance_valeur = value[5]
    
    nouveau_avance = global_frame.avance_entry_versement.get()
        
    if float(nouveau_avance) <= (float(prix_de_vente) - float(avance_valeur)):
        
        return float(avance_valeur) + float(nouveau_avance)
        
    else:
            
        messagebox.showerror('ERREUR', 'Vous avez depassé le prix de vente !!')
        
        return avance_valeur


def modifier_avance(payer_versements_tree):
    
    global global_frame
    
    try:
    
        selected = payer_versements_tree.focus()
        value = payer_versements_tree.item(selected, 'values')
        
        nouveau_avance = calculer_avance()
        
        facture_versement_db = sqlite3.connect('Facture_Versement.db')
        facture_versement_cursor = facture_versement_db.cursor()
        
        facture_versement_cursor.execute("""UPDATE Versement set
                                numero = :num,
                                prenom = :prenom,
                                nom = :nom,
                                cin = :cin,
                                prix_vente = :pv,
                                avance = :avance,
                                tel = :tel,
                                date_depart = :dd
                                WHERE numero = :id""",
                                {'num': value[0],
                                'prenom': value[1],
                                'nom': value[2],
                                'cin': value[3],
                                'pv': value[4],
                                'avance': nouveau_avance,
                                'tel': value[6],
                                'dd': value[7],
                                'id': value[0]
                                })
        
        facture_versement_db.commit()
        facture_versement_db.close()
        
        # update the treeview
        for record in payer_versements_tree.get_children():
            payer_versements_tree.delete(record)
            
        vider_versement()
        versement_database(payer_versements_tree)
        
    except:

        messagebox.showinfo('ERREUR', "Tu as oublié(e) de sélectionner le rocord!!\nSélectionnez-le s'il vous plait.")
    
    
def supprimer_tous_versement(payer_versements_tree):

    reponse = messagebox.askyesno('WHOOOA!!!', 'Cela supprimera tout du tableau\nêtes-vous sûr?')
        
    if reponse == 1:
            
        facture_versement_db = sqlite3.connect('Facture_Versement.db')
        facture_versement_cursor = facture_versement_db.cursor()
        
        facture_versement_cursor.execute('DROP TABLE Versement')
        facture_versement_cursor.execute('CREATE TABLE if not exists Versement(numero, prenom, nom, cin, prix_vente, avance, tel, date_depart)')
        
        facture_versement_db.commit()
        facture_versement_db.close()
            
        vider_versement()
            
        # update the treeview
        for record in payer_versements_tree.get_children():
            payer_versements_tree.delete(record)
            
            
def rechercher_versement(payer_versement_tree):
    
    global count
    
    but = global_frame.versement_recherche_entry.get()
    
    # update the treeview
    for record in payer_versement_tree.get_children():
        payer_versement_tree.delete(record)
    
    facture_versement_db = sqlite3.connect('Facture_Versement.db')
    facture_versement_cursor = facture_versement_db.cursor()
    
    facture_versement_cursor.execute('SELECT * from Versement WHERE numero like ? or prenom like ? or nom like ? or cin like ? or tel like ? or date_depart like ?', (but, but, but, but, but, but,))
    
    records = facture_versement_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            payer_versement_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags = ('evenrow',))
            
        else:
            
            payer_versement_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags = ('oddrow',))
            
        count += 1
        
    facture_versement_db.commit()
    facture_versement_db.close()
    
    vider_versement()
            
            
def refraichir_versement(payer_versements_tree):
    
    global count
    
    # update the treeview
    for record in payer_versements_tree.get_children():
        payer_versements_tree.delete(record)
    
    facture_versement_db = sqlite3.connect('Facture_Versement.db')
    facture_versement_cursor = facture_versement_db.cursor()
    
    facture_versement_cursor.execute('SELECT * from Versement')
    
    records = facture_versement_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            payer_versements_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags = ('evenrow',))
            
        else:
            
            payer_versements_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7]), tags = ('oddrow',))
            
        count += 1
        
    facture_versement_db.commit()
    facture_versement_db.close()
    
    vider_versement()
    
    
###-----------Bon Fonctions----------------------------------------------------------------------------------------------------------------------------------------------
        
    
def bon_database(bon_client_tree):
    
    global count
        
    # update the treeview
    for record in bon_client_tree.get_children():
        bon_client_tree.delete(record)
        
    bon_client_db = sqlite3.connect('Bon_Client.db')
    bon_client_cursor = bon_client_db.cursor()
    
    bon_client_cursor.execute('SELECT * FROM Bon')
        
    records = bon_client_cursor.fetchall()
    count = 0
        
    for record in records:
        
        if count % 2 == 0 :
            
            bon_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('evenrow',))
            
        else:
            
            bon_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('oddrow',))
                
        count += 1
            
    bon_client_db.commit()
    bon_client_db.close()
    
    
def vider_bon():
    
    global_frame.bon_nFacture_entry.delete(0, END)
    global_frame.bon_recherche_entry.delete(0, END)
    
    
def select_bon(event):
    
    vider_bon()
    
    selected = global_frame.bon_client_tree.focus()
    value = global_frame.bon_client_tree.item(selected, 'values')
    
    global_frame.bon_nFacture_entry.insert(0, value[0])
    
    
def supprimer_tous_bon(bon_client_tree):
    
    reponse = messagebox.askyesno('WHOOOA!!!', 'Cela supprimera tout du tableau\nêtes-vous sûr?')
        
    if reponse == 1:
            
        bon_client_db = sqlite3.connect('Bon_Client.db')
        bon_client_cursor = bon_client_db.cursor()
        
        bon_client_cursor.execute('DROP table Bon')
        bon_client_cursor.execute('CREATE TABLE if not exists Bon(numero, prenom, nom, cin, prix_vente, tel, date)')
        
        bon_client_db.commit()
        bon_client_db.close()
                
        vider_bon()
                
        # update the treeview
        for record in bon_client_tree.get_children():
            bon_client_tree.delete(record)
            
            
def rechercher_bon(bon_client_tree):
    
    global count
    
    but = global_frame.versement_recherche_entry.get()
    
    # update the treeview
    for record in bon_client_tree.get_children():
        bon_client_tree.delete(record)
    
    bon_client_db = sqlite3.connect('Bon_Client.db')
    bon_client_cursor = bon_client_db.cursor()
    
    bon_client_cursor.execute('SELECT * from Bon WHERE numero like ? or prenom like ? or nom like ? or cin like ? or tel like ? or date like ?', (but, but, but, but, but, but,))
    
    records = bon_client_cursor.fetchall()
    count = 0
    
    for record in records:
        if count % 2 == 0 :
            bon_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('evenrow',))
        else:
            bon_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('oddrow',))
            
        count += 1
        
    bon_client_db.commit()
    bon_client_db.close()
    
    vider_bon()
    
    
def refraichir_bon(bon_client_tree):
    
    global count
    
    # update the treeview
    for record in bon_client_tree.get_children():
        bon_client_tree.delete(record)
    
    bon_client_db = sqlite3.connect('Bon_Client.db')
    bon_client_cursor = bon_client_db.cursor()
    
    bon_client_cursor.execute('SELECT * from Bon')
    
    records = bon_client_cursor.fetchall()
    count = 0
    
    for record in records:
        if count % 2 == 0 :
            bon_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('evenrow',))
        else:
            bon_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('oddrow',))
            
        count += 1
        
    bon_client_db.commit()
    bon_client_db.close()
    
    vider_bon()
    
    
###-----------Mauvais Fonctions----------------------------------------------------------------------------------------------------------------------------------------------


def mauvais_database(mauvais_client_tree):
    
    global count
        
    # update the treeview
    for record in mauvais_client_tree.get_children():
        mauvais_client_tree.delete(record)
        
    mauvais_client_db = sqlite3.connect('Mauvais_Client.db')
    mauvais_client_cursor = mauvais_client_db.cursor()
    
    mauvais_client_cursor.execute('SELECT * FROM Mauvais')
        
    records = mauvais_client_cursor.fetchall()
    count = 0
        
    for record in records:
        
        if count % 2 == 0 :
            
            mauvais_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('evenrow',))
            
        else:
            
            mauvais_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('oddrow',))
                
        count += 1
            
    mauvais_client_db.commit()
    mauvais_client_db.close()
    
    
def vider_mauvais():
    
    global_frame.mauvais_nFacture_entry.delete(0, END)
    global_frame.mauvais_recherche_entry.delete(0, END)
    
    
def select_mauvais(event):
    
    vider_mauvais()
    
    selected = global_frame.mauvais_client_tree.focus()
    value = global_frame.mauvais_client_tree.item(selected, 'values')
    
    global_frame.mauvais_nFacture_entry.insert(0, value[0])
    
    
def supprimer_tous_mauvais(mauvais_client_tree):
    
    reponse = messagebox.askyesno('WHOOOA!!!', 'Cela supprimera tout du tableau\nêtes-vous sûr?')
        
    if reponse == 1:
            
        mauvais_client_db = sqlite3.connect('Mauvais_Client.db')
        mauvais_client_cursor = mauvais_client_db.cursor()
        
        mauvais_client_cursor.execute('DROP table Mauvais')
        mauvais_client_cursor.execute('CREATE TABLE if not exists Mauvais(numero, prenom, nom, cin, prix_non_payer, tel, date)')
        
        mauvais_client_db.commit()
        mauvais_client_db.close()
                
        vider_bon()
                
        # update the treeview
        for record in mauvais_client_tree.get_children():
            mauvais_client_tree.delete(record)
            
            
def rechercher_mauvais(mauvais_client_tree):
    
    global count
    
    but = global_frame.mauvais_recherche_entry.get()
    
    # update the treeview
    for record in mauvais_client_tree.get_children():
        mauvais_client_tree.delete(record)
    
    mauvais_client_db = sqlite3.connect('Mauvais_Client.db')
    mauvais_client_cursor = mauvais_client_db.cursor()
    
    mauvais_client_cursor.execute('SELECT * from Mauvais WHERE numero like ? or prenom like ? or nom like ? or cin like ? or tel like ? or date like ?', (but, but, but, but, but, but,))
    
    records = mauvais_client_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            mauvais_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('evenrow',))
            
        else:
            
            mauvais_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('oddrow',))
            
        count += 1
        
    mauvais_client_db.commit()
    mauvais_client_db.close()
    
    vider_mauvais()
    
    
def refraichir_mauvais(mauvais_client_tree):
    
    global count
    
    # update the treeview
    for record in mauvais_client_tree.get_children():
        mauvais_client_tree.delete(record)
    
    mauvais_client_db = sqlite3.connect('Mauvais_Client.db')
    mauvais_client_cursor = mauvais_client_db.cursor()
    
    mauvais_client_cursor.execute('SELECT * from Mauvais')
    
    records = mauvais_client_cursor.fetchall()
    count = 0
    
    for record in records:
        
        if count % 2 == 0 :
            
            mauvais_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('evenrow',))
            
        else:
            
            mauvais_client_tree.insert(parent = '', index = 'end', iid = count, text = '', values = (record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags = ('oddrow',))
            
        count += 1
        
    mauvais_client_db.commit()
    mauvais_client_db.close()
    
    vider_mauvais()
    
    
###-----------Client bill Fonctions----------------------------------------------------------------------------------------------------------------------------------------------


def bill_number():
    
    n1 = random.randint(10, 10000)
    n2 = random.randint(10, 10000)
    n3 = random.randint(10, 10000)

    return n1 + n2 + n3


def ajouter_facture():
    
    global global_frame, v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11
    
    v1 = global_frame.prenom_entry.get()
    v2 = global_frame.nom_entry.get()
    v3 = global_frame.marque_entry.get()
    v4 = global_frame.model_entry.get()
    v5 = global_frame.type_entry.get()
    v6 = global_frame.utiliser_entry.get()
    v7 = global_frame.cpu_entry.get()
    v8 = global_frame.stockage_entry.get()
    v9 = global_frame.ram_entry.get()
    v10 = global_frame.tel_entry.get()
    v11 = global_frame.date_entry.get()
    
    Accueil.destroy_menu(global_frame)
    Client.destroy_client(global_frame)
    Stock.destroy_stock(global_frame)
    Facture.destroy_facture(global_frame)
    
    global_frame = client_bill()
    
    global x, d
    
    date = (datetime.datetime.now())
    d = date.strftime('%x')
    x = bill_number()
    
    global_frame.bill.insert('insert','\n\n Numero de Facture : b{}\t\t\t\t\t\t\tSAFI le : {}'.format(x, d))
    global_frame.bill.insert('insert','\n\n Client : {}\t\t\t\t\t\tCIN : {}'.format(v2+' '+v1, global_frame.cin_box))
    global_frame.bill.insert('insert','\n\n Tel : {}'.format(v10))
    global_frame.bill.insert('insert',"\n\n_______________________________________________________________________________")
    global_frame.bill.insert('insert','\n\n Prix Unité \t\t\t Quantite \t\t\t Prix Total\n'.format())
    global_frame.bill.insert('insert',"_______________________________________________________________________________")
    
    
def calculer_prix():
    
    global prix_total
    
    prix = float(global_frame.prix_entry.get())
    quantite = int(global_frame.quantite_entry.get())
    
    prix_total = prix * quantite
    
    return prix_total
    
    
def ajouter_au_facture():
    
    global prix, quantite, prix_total, supprimer_window
    
    try:
        
        prix = global_frame.prix_entry.get()
        quantite = int(global_frame.quantite_entry.get())
            
        if quantite < 1:
        
            messagebox.showinfo('ERREUR', "La quantité Ne convient Pas, la quantité inferieur à 1!!\nTape une quantité compris s'il vous plait.")
                
        elif quantite == 1:
            
            prix_total = calculer_prix()
                
            global_frame.bill.insert('insert','\n\n {} \t\t\t {} \t\t\t {}'.format(prix, quantite, prix_total))
                
            appareil = global_frame.appareil_entry.get()
            supprimer_appareil(appareil)
                
        else:
            
            prix_total = calculer_prix()
                
            global_frame.bill.insert('insert','\n\n {} \t\t\t {} \t\t\t {}'.format(prix, quantite, prix_total))
            
            supprimer_window = Toplevel(window)
    
            supprimer_window.title('Supprimer')
            supprimer_window.geometry('')
            
            app_code_label = customtkinter.CTkLabel(supprimer_window, text='Appareil Code :', text_color='black')
            app_code_label.pack(padx = 10, pady = 10)
            app_code_entry = customtkinter.CTkEntry(supprimer_window, placeholder_text='...')
            app_code_entry.pack(padx = 10, pady = 10)
            
            app_button = customtkinter.CTkButton(supprimer_window, text='Supprimer', command= lambda: supprimer_appareil(app_code_entry.get()))
            app_button.pack(padx = 10, pady = 10)
            
            supprimer_window.mainloop()
            
    except:
        
        messagebox.showinfo('ERREUR', "Tu as oublié(e) de tape le prix ou(et) la quantité !!\nTape-les s'il vous plait.")
        
        
def supprimer_appareil(appareil):
    
    if appareil == '':
        
        messagebox.showinfo('ERREUR', "Tu as oublié(e) de tape le code d'appareil !!\nTape-le s'il vous plait.")
        
    else:
        
        stock_db = sqlite3.connect('Stock.db')
        stock_cursor =  stock_db.cursor()
        
        stock_cursor.execute('SELECT EXISTS (SELECT 1 FROM Stock WHERE code like ?)',(appareil,))
        
        data = stock_cursor.fetchone()[0]
        
        if data == 0:
            
            messagebox.showinfo('ERREUR', "Il n'existe aucun appareil avec ce code!\nVeuillez vérifier à nouveau votre code s'il vous plait.")
            
        else:
            
            stock_cursor.execute('DELETE from Stock WHERE code = ?', (appareil,))
            stock_cursor.execute('CREATE TABLE if not exists Stock(code, marque, model, type, utiliser, os, cpu, gpu, stockage, ram, prix_achat, prix_vente)')
        
        stock_db.commit()
        stock_db.close()
    
    
def vider_bill():
    
    global_frame.prix_entry.delete(0, END)
    global_frame.quantite_entry.delete(0, END)
    global_frame.appareil_entry.delete(0, END)
    

def souvegarder():
    
    global choix, avance_entry, souvegarder_window, prix_total
    
    souvegarder_window = Toplevel(window)
    
    souvegarder_window.title('Souvegarde')
    souvegarder_window.geometry('')
    
    choix = customtkinter.IntVar()
    
    radiobutton1 = customtkinter.CTkRadioButton(souvegarder_window, text='Payer Cash', variable=choix, value=1, text_color='black')
    radiobutton1.pack(padx = 10, pady = 10)
    radiobutton2 = customtkinter.CTkRadioButton(souvegarder_window, text='Payer Versement', variable=choix, value=2, text_color='black')
    radiobutton2.pack(padx = 10, pady = 10)
    
    avance_label = customtkinter.CTkLabel(souvegarder_window, text='Avance (en cas non payer cash)', text_color='black')
    avance_label.pack(padx = 10, pady = 10)
    avance_entry = customtkinter.CTkEntry(souvegarder_window, placeholder_text='...')
    avance_entry.pack(padx = 10, pady = 10)
    
    souvegarder_button = customtkinter.CTkButton(souvegarder_window, text='Valider', font=customtkinter.CTkFont('arial', 15, 'bold'), command= lambda: ajouter_cash_ou_versement(choix))
    souvegarder_button.pack(padx = 10, pady = 10)
    
    
def ajouter_cash_ou_versement(choix):
    
    global avance_entry, souvegarder_window, x, d, v1, v2, prix_total, v10, av_e
    
    av_e = avance_entry.get()
    
    if av_e == '':
        
        av_e = 0
    
    souvegarder_window.destroy()
    
    if choix.get() == 1:
        
        facture_cash_db = sqlite3.connect('Facture_Cash.db')
        facture_cash_cursor = facture_cash_db.cursor()
        
        facture_cash_cursor.execute("""INSERT INTO Cash VALUES (:numero, :prenom, :nom, :cin, :prix_vente, :tel, :date)""",
                        {
                            'numero': ("b{}".format(x)),
                            'prenom': v1,
                            'nom': v2,
                            'cin': global_frame.cin_box,
                            'prix_vente': prix_total,
                            'tel': v10,
                            'date': d
                        }
                        )
        
        facture_cash_db.commit()
        facture_cash_db.close()
        
    else:
        
        facture_versement_db = sqlite3.connect('Facture_Versement.db')
        facture_versement_cursor = facture_versement_db.cursor()
        
        facture_versement_cursor.execute('CREATE TABLE if not exists Versement(numero, prenom, nom, cin, prix_vente, avance, tel, date_depart)')
        facture_versement_cursor.execute("""INSERT INTO Versement VALUES (:numero, :prenom, :nom, :cin, :prix_vente, :avance, :tel, :date_depart)""",
                            {
                                'numero': ("b{}".format(x)),
                                'prenom': v1,
                                'nom': v2,
                                'cin': global_frame.cin_box,
                                'prix_vente': prix_total,
                                'avance': av_e,
                                'tel': v10,
                                'date_depart': d
                            }
                            )
        
        facture_versement_db.commit()
        facture_versement_db.close()
        
    vider_bill()
    
    
###-----------Cash bill Fonctions----------------------------------------------------------------------------------------------------------------------------------------------


def ouvrir_cash():
    
    try:
    
        global global_frame, val1, val2, val3, val4, val5, val6, val7
        
        selected = global_frame.payer_cash_tree.focus()
        value = global_frame.payer_cash_tree.item(selected, 'values')
        
        val1 = global_frame.nFacture_entry_cash.get()
            
        facture_cash_db = sqlite3.connect('Facture_Cash.db')
        facture_cash_cursor = facture_cash_db.cursor()
            
        facture_cash_cursor.execute('SELECT EXISTS (SELECT * FROM Cash WHERE numero like ?)', (val1,))
            
        data = facture_cash_cursor.fetchone()[0]
            
        if data == 0:
                
            messagebox.showinfo('ERREUR', "Il n'existe aucun Client avec ce numéro de facture!\nVeuillez vérifier à nouveau votre numéro de facture s'il vous plait.")
                
        else:
            
            facture_cash_cursor.execute('SELECT * FROM Cash WHERE numero like ?', (val1,))
            
            records = facture_cash_cursor.fetchall()
            
            for record in records:
            
                val2 = record[1]
                val3 = record[2]
                val4 = record[3]
                val5 = record[4]
                val6 = record[5]
                val7 = record[6]
                
            Accueil.destroy_menu(global_frame)
            Client.destroy_client(global_frame)
            Stock.destroy_stock(global_frame)
            Facture.destroy_facture(global_frame)
            client_bill.destroy_client_bill(global_frame)
            
            global_frame = cash_bill()
                
            global_frame.cash_bill.insert('insert','\n\n Numero de Facture : b{}\t\t\t\t\t\t\tSAFI le : {}'.format(val1, val7))
            global_frame.cash_bill.insert('insert','\n\n Client : {}\t\t\t\t\t\tCIN : {}'.format(val2+' '+val3, val4))
            global_frame.cash_bill.insert('insert','\n\n Tel : {}\n'.format(val6))
            global_frame.cash_bill.insert('insert',"_______________________________________________________________________________")
            global_frame.cash_bill.insert('insert','\n\n Prix Total\n'.format())
            global_frame.cash_bill.insert('insert',"_______________________________________________________________________________")
            global_frame.cash_bill.insert('insert','\n\n {}\n'.format(val5))
                
        facture_cash_db.commit()
        facture_cash_db.close()
        
    except:
        
        messagebox.showinfo('ERREUR', "Tu as oublié(e) de sélectionner le rocord!!\nSélectionnez-le s'il vous plait.")
        
        
def fermer_cash():
    
    global global_frame
    
    cash_bill.destroy_cash_bill(global_frame)
    global_frame =  Facture()
    
    
###-----------Versement bill Fonctions----------------------------------------------------------------------------------------------------------------------------------------------
    
    
def ouvrir_versement():
    
    try:
    
        global global_frame, val1, val2, val3, val4, val5, val6, val7, val8, valeur1, valeur2, valeur3, valeur4, valeur5, valeur6, valeur7
        
        selected = global_frame.payer_versements_tree.focus()
        value = global_frame.payer_versements_tree.item(selected, 'values')
        
        val1 = global_frame.nFacture_entry_versement.get()
        
        facture_versement_db = sqlite3.connect('Facture_Versement.db')
        facture_versement_cursor = facture_versement_db.cursor()
        
        facture_versement_cursor.execute('SELECT EXISTS (SELECT numero FROM Versement WHERE numero like ?)', (val1,))
        
        data = facture_versement_cursor.fetchone()[0]
        
        if data == 0:
            
            messagebox.showinfo('ERREUR', "Il n'existe aucun Client avec ce numéro de facture!\nVeuillez vérifier à nouveau votre numéro de facture s'il vous plait.")
            
        else:
            
            facture_versement_cursor.execute('SELECT * from Versement WHERE numero like ?',(val1,))
            
            records = facture_versement_cursor.fetchall()
            
            for record in records:
                
                val2 = record[1]
                val3 = record[2]
                val4 = record[3]
                val5 = record[4]
                val6 = record[5]
                val7 = record[6]
                val8 = record[7]
            
            Accueil.destroy_menu(global_frame)
            Client.destroy_client(global_frame)
            Stock.destroy_stock(global_frame)
            Facture.destroy_facture(global_frame)
            client_bill.destroy_client_bill(global_frame)
            
            global_frame = versement_bill()
            
            global_frame.versement_bill.insert('insert','\n\n Numero de Facture : b{}\t\t\t\t\t\t\tSAFI le : {}'.format(val1, val8))
            global_frame.versement_bill.insert('insert','\n\n Client : {}\t\t\t\t\t\tCIN : {}'.format(val2+' '+val3, val4))
            global_frame.versement_bill.insert('insert','\n\n Tel : {}\n'.format(val7))
            global_frame.versement_bill.insert('insert',"_______________________________________________________________________________")
            global_frame.versement_bill.insert('insert','\n\n Prix Total\t\t\tAvance\n'.format())
            global_frame.versement_bill.insert('insert',"_______________________________________________________________________________")
            global_frame.versement_bill.insert('insert','\n\n {}\t\t\t{}\n'.format(val5, val6))
            
            valeur1 = val1
            valeur2 = val2
            valeur3 = val3
            valeur4 = val4
            valeur5 = val6
            valeur6 = val7
            valeur7 = val8
            
        facture_versement_db.commit()
        facture_versement_db.close()
        
    except:
        
        messagebox.showinfo('ERREUR', "Tu as oublié(e) de sélectionner le rocord!!\nSélectionnez-le s'il vous plait.")
        
        
def fermer_versement():
    
    global global_frame
    
    versement_bill.destroy_versement_bill(global_frame)
    global_frame =  Facture()
    
    
###-----------Bon bill Fonctions----------------------------------------------------------------------------------------------------------------------------------------------
        
        
def ajouter_bon():
    
        global global_frame, valeur1, valeur2, valeur3, valeur4, valeur5, valeur6, valeur7
        
        bon_client_db = sqlite3.connect('Bon_Client.db')
        bon_client_cursor = bon_client_db.cursor()
        
        bon_client_cursor.execute("""INSERT INTO Bon VALUES (:numero, :prenom, :nom, :cin, :prix_vente, :tel, :date)""",
                                {'numero': valeur1,
                                 'prenom': valeur2,
                                 'nom': valeur3,
                                 'cin': valeur4,
                                 'prix_vente': valeur5,
                                 'tel': valeur6,
                                 'date': valeur7  
                                })
        
        bon_client_db.commit()
        bon_client_db.close()
        
        messagebox.showinfo('SUCCES', 'Ajouté avec succès au la liste de Bon Client.')
        
        facture_versement_db = sqlite3.connect('Facture_Versement.db')
        facture_versement_cursor = facture_versement_db.cursor()
        
        facture_versement_cursor.execute('DELETE from Versement WHERE numero like ?', (valeur1,))
        
        facture_versement_db.commit()
        facture_versement_db.close()
        
        versement_bill.destroy_versement_bill(global_frame)
        
        global_frame = Facture()
    
    
def ouvrir_bon():
    
    try:
    
        global global_frame, val1, val2, val3, val4, val5, val6, val7
        
        selected = global_frame.bon_client_tree.focus()
        value = global_frame.bon_client_tree.item(selected, 'values')
        
        val1 = global_frame.bon_nFacture_entry.get()
        
        bon_client_db = sqlite3.connect('Bon_Client.db')
        bon_client_cursor = bon_client_db.cursor()
        
        bon_client_cursor.execute('SELECT EXISTS (SELECT numero FROM Bon WHERE numero like ?)',(val1,))
        
        data = bon_client_cursor.fetchone()[0]
        
        if data == 0:
            
            messagebox.showinfo('ERREUR', "Il n'existe aucun Client avec ce numéro de facture!\nVeuillez vérifier à nouveau votre numéro de facture s'il vous plait.")
            
        else:
            
            bon_client_cursor.execute('SELECT * from Bon WHERE numero like ?', (val1,))
            
            records = bon_client_cursor.fetchall()
            
            for record in records:
                
                val2 = record[1]
                val3 = record[2]
                val4 = record[3]
                val5 = record[4]
                val6 = record[5]
                val7 = record[6]
            
            Accueil.destroy_menu(global_frame)
            Client.destroy_client(global_frame)
            Stock.destroy_stock(global_frame)
            Facture.destroy_facture(global_frame)
            client_bill.destroy_client_bill(global_frame)
            versement_bill.destroy_versement_bill(global_frame)
            
            global_frame = bon_bill()
            
            global_frame.bon_bill.insert('insert','\n\n Numero de Facture : b{}\t\t\t\t\t\t\tSAFI le : {}'.format(val1, val7))
            global_frame.bon_bill.insert('insert','\n\n Client : {}\t\t\t\t\t\tCIN : {}'.format(val2+' '+val3, val4))
            global_frame.bon_bill.insert('insert','\n\n Tel : {}\n'.format(val6))
            global_frame.bon_bill.insert('insert',"_______________________________________________________________________________")
            global_frame.bon_bill.insert('insert','\n\n Prix Total\n'.format())
            global_frame.bon_bill.insert('insert',"_______________________________________________________________________________")
            global_frame.bon_bill.insert('insert','\n\n {}\n'.format(val5))
            
        bon_client_db.commit()
        bon_client_db.close()
        
    except:
        
        messagebox.showinfo('ERREUR', "Tu as oublié(e) de sélectionner le rocord!!\nSélectionnez-le s'il vous plait.")
        

def fermer_bon():
    
    global global_frame
    
    bon_bill.destroy_bon_bill(global_frame)
    global_frame =  Facture()
    
    
###-----------Mauvais bill Fonctions----------------------------------------------------------------------------------------------------------------------------------------------
    
    
def calculer_prix_non_payer():
    
    global global_frame, val5, val6
    
    return float(val5) - float(val6)
    
    
def ajouter_mauvais():
    
        global global_frame, valeur1, valeur2, valeur3, valeur4, valeur5, valeur6, valeur7
        
        valeur5 = calculer_prix_non_payer()
        
        mauvais_client_db = sqlite3.connect('Mauvais_Client.db')
        mauvais_client_cursor = mauvais_client_db.cursor()
        
        mauvais_client_cursor.execute("""INSERT INTO Mauvais VALUES (:numero, :prenom, :nom, :cin, :prix_non_payer, :tel, :date)""",
                                {'numero': valeur1,
                                 'prenom': valeur2,
                                 'nom': valeur3,
                                 'cin': valeur4,
                                 'prix_non_payer': valeur5,
                                 'tel': valeur6,
                                 'date': valeur7  
                                })
        
        mauvais_client_db.commit()
        mauvais_client_db.close()
        
        messagebox.showinfo('SUCCES', 'Ajouté avec succès au la liste de Mauvais Client.')
        
        facture_versement_db = sqlite3.connect('Facture_Versement.db')
        facture_versement_cursor = facture_versement_db.cursor()
        
        facture_versement_cursor.execute('DELETE from Versement WHERE numero like ?', (valeur1,))
        
        facture_versement_db.commit()
        facture_versement_db.close()
        
        versement_bill.destroy_versement_bill(global_frame)
        
        global_frame = Facture()
    
    
def ouvrir_mauvais():
    
    try:
    
        global global_frame, val1, val2, val3, val4, val5, val6, val7
        
        selected = global_frame.mauvais_client_tree.focus()
        value = global_frame.mauvais_client_tree.item(selected, 'values')
        
        val1 = global_frame.mauvais_nFacture_entry.get()
        
        mauvais_client_db = sqlite3.connect('Mauvais_Client.db')
        mauvais_client_cursor = mauvais_client_db.cursor()
        
        mauvais_client_cursor.execute('SELECT EXISTS (SELECT numero FROM Mauvais WHERE numero like ?)', (val1,))
        
        data = mauvais_client_cursor.fetchone()[0]
        
        if data == 0:
            
             messagebox.showinfo('ERREUR', "Il n'existe aucun Client avec ce numéro de facture!\nVeuillez vérifier à nouveau votre numéro de facture s'il vous plait.")
            
        else:
            
            mauvais_client_cursor.execute('SELECT * from Mauvais WHERE numero like ?', (val1,))
            
            records = mauvais_client_cursor.fetchall()
            
            for record in records:
                
                val2 = record[1]
                val3 = record[2]
                val4 = record[3]
                val5 = record[4]
                val6 = record[5]
                val7 = record[6]
            
            Accueil.destroy_menu(global_frame)
            Client.destroy_client(global_frame)
            Stock.destroy_stock(global_frame)
            Facture.destroy_facture(global_frame)
            client_bill.destroy_client_bill(global_frame)
            versement_bill.destroy_versement_bill(global_frame)
            bon_bill.destroy_bon_bill(global_frame)
            
            global_frame = mauvais_bill()
            
            global_frame.mauvais_bill.insert('insert','\n\n Numero de Facture : b{}\t\t\t\t\t\t\tSAFI le : {}'.format(val1, val7))
            global_frame.mauvais_bill.insert('insert','\n\n Client : {}\t\t\t\t\t\tCIN : {}'.format(val2+' '+val3, val4))
            global_frame.mauvais_bill.insert('insert','\n\n Tel : {}\n'.format(val6))
            global_frame.mauvais_bill.insert('insert',"_______________________________________________________________________________")
            global_frame.mauvais_bill.insert('insert','\n\n Prix non payer\n'.format())
            global_frame.mauvais_bill.insert('insert',"_______________________________________________________________________________")
            global_frame.mauvais_bill.insert('insert','\n\n {}\n'.format(val5))
            
        mauvais_client_db.commit()
        mauvais_client_db.close()
        
    except:
        
        messagebox.showinfo('ERREUR', "Tu as oublié(e) de sélectionner le rocord!!\nSélectionnez-le s'il vous plait.")
        
        
def fermer_mauvais():
    
    global global_frame
    
    mauvais_bill.destroy_mauvais_bill(global_frame)
    global_frame =  Facture()


class Accueil:
    
    def __init__(self) -> None:
        
        self.store_image = customtkinter.CTkImage(light_image=Image.open('ERP(PC-Store)/PC-store-icon.png'), dark_image=Image.open('ERP(PC-Store)/PC-store-icon.png'), size=(575, 192))
        
        self.menu_frame = customtkinter.CTkFrame(window, height=100, corner_radius=0)
        self.menu_frame.grid(row=0, column=0, sticky = 'nsew')
        self.theme_option = customtkinter.CTkOptionMenu(self.menu_frame, width=150, height=30, values=['system','Light','Dark'], command=self.change_theme_mode)
        self.theme_option.grid(row=0, column=0, padx=10, pady=10)
        self.menu_name = customtkinter.CTkLabel(self.menu_frame, text='Menu', text_color=('black', 'white'), font=('helvetica', 30))
        self.menu_name.grid(row=0, column=1,  pady=10, sticky='nsew')
        self.accueil_button = customtkinter.CTkButton(self.menu_frame, width=150, height=30, text='Accueil', font=customtkinter.CTkFont(size=15, weight='bold'), command=accueil_frame)
        self.accueil_button.grid(row = 0, column = 2, pady = 10)

        self.client_button = customtkinter.CTkButton(self.menu_frame, width=150, height=30, text='Client', font=customtkinter.CTkFont(size=15, weight='bold'), command=client_frame)
        self.client_button.grid(row = 1, column = 0, padx = 116, pady = 10, sticky='nsew')
        self.stock_button = customtkinter.CTkButton(self.menu_frame, width=150, height=30, text='Stock', font=customtkinter.CTkFont(size=15, weight='bold'), command=stock_frame)
        self.stock_button.grid(row = 1, column = 1, padx = 117, pady = 10, sticky='nsew')
        self.facture_button = customtkinter.CTkButton(self.menu_frame, width=150, height=30, text='Facture', font=customtkinter.CTkFont(size=15, weight='bold'), command=facture_frame)
        self.facture_button.grid(row = 1, column = 2, padx = 117, pady = 10, sticky='nsew')
        
        self.image_label = customtkinter.CTkLabel(window, text='', image=self.store_image)
        self.image_label.grid(padx=10, pady=150)
        
        
    def change_theme_mode(self, new_theme_mode):
        
        customtkinter.set_appearance_mode(new_theme_mode)
        
        
    def destroy_menu(self):
        
        for widget in window.winfo_children():            
            widget.destroy()


class Menu:
    
    def __init__(self) -> None:
        
        self.menu_frame = customtkinter.CTkFrame(window, height=100, corner_radius=0)
        self.menu_frame.grid(row=0, column=0, sticky = 'nsew')
        self.theme_option = customtkinter.CTkOptionMenu(self.menu_frame, width=150, height=30, values=['system','Light','Dark'], command=self.change_theme_mode)
        self.theme_option.grid(row=0, column=0, padx=10, pady=10)
        self.menu_name = customtkinter.CTkLabel(self.menu_frame, text='Menu', text_color=('black', 'white'), font=('helvetica', 30))
        self.menu_name.grid(row=0, column=1,  pady=10, sticky='we')
        self.accueil_button = customtkinter.CTkButton(self.menu_frame, width=150, height=30, text='Accueil', font=customtkinter.CTkFont(size=15, weight='bold'), command=accueil_frame)
        self.accueil_button.grid(row = 0, column = 2, pady = 10)

        self.client_button = customtkinter.CTkButton(self.menu_frame, width=150, height=30, text='Client', font=customtkinter.CTkFont(size=15, weight='bold'), command=client_frame)
        self.client_button.grid(row = 1, column = 0, padx = 116, pady = 10)
        self.stock_button = customtkinter.CTkButton(self.menu_frame, width=150, height=30, text='Stock', font=customtkinter.CTkFont(size=15, weight='bold'), command=stock_frame)
        self.stock_button.grid(row = 1, column = 1, padx = 117, pady = 10)
        self.facture_button = customtkinter.CTkButton(self.menu_frame, width=150, height=30, text='Facture', font=customtkinter.CTkFont(size=15, weight='bold'), command=facture_frame)
        self.facture_button.grid(row = 1, column = 2, padx = 117, pady = 10)
        
        
    def change_theme_mode(self, new_theme_mode):
        
        customtkinter.set_appearance_mode(new_theme_mode)
          
    
    def destroy_menu(self):
        
        for widget in window.winfo_children():
            widget.destroy()


class Client:
    
    def __init__(self) -> None:
        
        self.menu = Menu()
        
        self.tabview = customtkinter.CTkTabview(window, height=480)
        self.tabview.grid(row = 1, column = 0, sticky = 'nsew')
        self.tabview.add('Nouveau Demande')
        self.tabview.add('Les Demandes')
        self.tabview.tab('Nouveau Demande').grid_columnconfigure(10, weight=1)
        
        ###-------------------TAB Nouveau Demande
        self.n_prenom_lebel = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='Prenom*:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.n_prenom_lebel.grid(row = 0, column = 0)
        self.n_prenom_entry = customtkinter.CTkEntry(self.tabview.tab('Nouveau Demande'), width=300, height=30, placeholder_text='...')
        self.n_prenom_entry.grid(row = 0, column = 1, padx = (10, 20), pady = 20)
        
        self.n_nom_lebel = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='Nom*:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.n_nom_lebel.grid(row = 1, column = 0)
        self.n_nom_entry = customtkinter.CTkEntry(self.tabview.tab('Nouveau Demande'), width=300, height=30, placeholder_text='...')
        self.n_nom_entry.grid(row = 1, column = 1, padx = (10, 20), pady = 20)
        
        self.n_marque_lebel = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='Marque:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.n_marque_lebel.grid(row = 2, column = 0)
        self.n_marque_entry = customtkinter.CTkEntry(self.tabview.tab('Nouveau Demande'), width=300, height=30, placeholder_text='...')
        self.n_marque_entry.grid(row = 2, column = 1, padx = (10, 20), pady = 20)
        
        self.n_model_lebel = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='Model:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.n_model_lebel.grid(row = 3, column = 0)
        self.n_model_entry = customtkinter.CTkEntry(self.tabview.tab('Nouveau Demande'), width=300, placeholder_text='...')
        self.n_model_entry.grid(row = 3, column = 1, padx = (10, 20), pady = 20)
        
        self.n_type_lebel = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='Type*:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.n_type_lebel.grid(row = 4, column = 0)
        self.n_type_entry = customtkinter.CTkEntry(self.tabview.tab('Nouveau Demande'), width=300, placeholder_text='...')
        self.n_type_entry.grid(row = 4, column = 1, padx = (10, 20), pady = 20)
        
        self.n_utiliser_lebel = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='Utiliser*:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.n_utiliser_lebel.grid(row = 5, column = 0)
        self.n_utiliser_entry = customtkinter.CTkEntry(self.tabview.tab('Nouveau Demande'), width=300, placeholder_text='...')
        self.n_utiliser_entry.grid(row = 5, column = 1, padx = (10, 20), pady = 20)
        
        self.n_cpu_lebel = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='CPU*:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.n_cpu_lebel.grid(row = 0, column = 2, padx = 20)
        self.n_cpu_entry = customtkinter.CTkEntry(self.tabview.tab('Nouveau Demande'), width=300, placeholder_text='...')
        self.n_cpu_entry.grid(row = 0, column = 3, padx = 10, pady = 20)
        
        self.n_stockage_lebel = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='Stockage:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.n_stockage_lebel.grid(row = 1, column = 2, padx = 20)
        self.n_stockage_entry = customtkinter.CTkEntry(self.tabview.tab('Nouveau Demande'), width=300, placeholder_text='...')
        self.n_stockage_entry.grid(row = 1, column = 3, padx = 10, pady = 20)
        
        self.n_ram_lebel = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='RAM*:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.n_ram_lebel.grid(row = 2, column = 2, padx = 20)
        self.n_ram_entry = customtkinter.CTkEntry(self.tabview.tab('Nouveau Demande'), width=300, placeholder_text='...')
        self.n_ram_entry.grid(row = 2, column = 3, padx = 10, pady = 20)
        
        self.n_tel_lebel = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='Tel*:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.n_tel_lebel.grid(row = 3, column = 2, padx = 20)
        self.n_tel_entry = customtkinter.CTkEntry(self.tabview.tab('Nouveau Demande'), width=300, placeholder_text='...')
        self.n_tel_entry.grid(row = 3, column = 3, padx = 10, pady = 20)
        
        self.n_date_label = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='Date*:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.n_date_label.grid(row = 4, column = 2, padx = 20)
        self.n_date_entry = customtkinter.CTkEntry(self.tabview.tab('Nouveau Demande'), width=300, placeholder_text='...')
        self.n_date_entry.grid(row = 4, column = 3, padx= 10, pady = 20)
        
        self.required_infos = customtkinter.CTkLabel(self.tabview.tab('Nouveau Demande'), text='*Important de saisir', text_color='red', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.required_infos.grid(row = 5, column = 2)
        
        self.ajouter_button = customtkinter.CTkButton(self.tabview.tab('Nouveau Demande'), text='Ajouter', corner_radius=10, fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, hover_color='green', command=ajouter_nouveau_client)
        self.ajouter_button.grid(row = 5, column = 3, padx = 30)
        
        ###-------------------TAB Les Demandes
        self.record_frame = customtkinter.CTkFrame(self.tabview.tab('Les Demandes'), width=380, height=380)
        self.record_frame.grid(row = 0, column = 0, rowspan = 11, sticky = 'nsew')
        
        self.prenom_lebel = customtkinter.CTkLabel(self.record_frame, text='Prenom*:')
        self.prenom_lebel.grid(row = 0, column = 0, padx = 65)
        self.prenom_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.prenom_entry.grid(row = 1, column = 0, padx = 10, pady = 2)
        
        self.nom_lebel = customtkinter.CTkLabel(self.record_frame, text='Nom*:')
        self.nom_lebel.grid(row = 0, column = 1, padx = 65)
        self.nom_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.nom_entry.grid(row = 1, column = 1, padx = 10, pady = 2)
        
        self.marque_lebel = customtkinter.CTkLabel(self.record_frame, text='Marque:')
        self.marque_lebel.grid(row = 2, column = 0, padx = 65)
        self.marque_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.marque_entry.grid(row = 3, column = 0, padx = 10, pady = 2)
        
        self.model_lebel = customtkinter.CTkLabel(self.record_frame, text='Model:')
        self.model_lebel.grid(row = 2, column = 1, padx = 65)
        self.model_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.model_entry.grid(row = 3, column = 1, padx = 10, pady = 2)
        
        self.type_lebel = customtkinter.CTkLabel(self.record_frame, text='Type*:')
        self.type_lebel.grid(row = 4, column = 0, padx = 65)
        self.type_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.type_entry.grid(row = 5, column = 0, padx = 10, pady = 2)
        
        self.utiliser_lebel = customtkinter.CTkLabel(self.record_frame, text='Utiliser*:')
        self.utiliser_lebel.grid(row = 4, column = 1, padx = 65)
        self.utiliser_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.utiliser_entry.grid(row = 5, column = 1, padx = 10, pady = 2)
        
        self.cpu_lebel = customtkinter.CTkLabel(self.record_frame, text='CPU*:')
        self.cpu_lebel.grid(row = 6, column = 0, padx = 65)
        self.cpu_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.cpu_entry.grid(row = 7, column = 0, padx = 10, pady = 2)
        
        self.stockage_lebel = customtkinter.CTkLabel(self.record_frame, text='Stockage:')
        self.stockage_lebel.grid(row = 6, column = 1, padx = 65)
        self.stockage_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.stockage_entry.grid(row = 7, column = 1, padx = 10, pady = 2)
        
        self.ram_lebel = customtkinter.CTkLabel(self.record_frame, text='RAM*:')
        self.ram_lebel.grid(row = 8, column = 0, padx = 65)
        self.ram_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.ram_entry.grid(row = 9, column = 0, padx = 10, pady = 2)
        
        self.tel_lebel = customtkinter.CTkLabel(self.record_frame, text='Tel*:')
        self.tel_lebel.grid(row = 8, column = 1, padx = 65)
        self.tel_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.tel_entry.grid(row = 9, column = 1, padx = 10, pady = 2)
        
        self.date_label = customtkinter.CTkLabel(self.record_frame, text='Date*:')
        self.date_label.grid(row = 10, column = 0, padx = 65)
        self.date_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.date_entry.grid(row = 11, column = 0, padx= 10, pady = 2)
        
        self.required_infos = customtkinter.CTkLabel(self.record_frame, text='*Important de saisir', text_color='red', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.required_infos.grid(row = 11, column = 1)
        
        self.tree_frame = customtkinter.CTkFrame(self.tabview.tab('Les Demandes'))
        self.tree_frame.grid(row = 0, column = 3, sticky = 'nsew')
        
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('treeview',
                background='#D3D3D3',
                foreground='black',
                rowheight=25,
                fieldbackground='#D3D3D3')
        self.style.map('treeview',
                background=[('selected', '#347083')])
        
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        
        self.client_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll, selectmode='extended', height=15)
        self.client_tree.pack()
        
        self.tree_scroll.config(command=self.client_tree.yview)
        self.client_tree['columns'] = ('ID', 'Prenom', 'Nom', 'Marque', 'Model', 'Type', 'Utiliser', 'CPU', 'Stockage', 'RAM', 'Tel', 'Date')
        
        self.client_tree.column('#0', width=0, stretch=NO)
        self.client_tree.column('ID', anchor=W, width=20)
        self.client_tree.column('Prenom', anchor=CENTER, width=130)
        self.client_tree.column('Nom', anchor=CENTER, width=130)
        self.client_tree.column('Marque', anchor=CENTER, width=110)
        self.client_tree.column('Model', anchor=CENTER, width=100)
        self.client_tree.column('Type', anchor=CENTER, width=80)
        self.client_tree.column('Utiliser', anchor=CENTER, width=70)
        self.client_tree.column('CPU', anchor=CENTER, width=100)
        self.client_tree.column('Stockage', anchor=CENTER, width=80)
        self.client_tree.column('RAM', anchor=CENTER, width=50)
        self.client_tree.column('Tel', anchor=CENTER, width=140)
        self.client_tree.column('Date', anchor=CENTER, width=90)
        
        self.client_tree.heading('#0', text='', anchor=W)
        self.client_tree.heading('ID', text='ID', anchor=CENTER)
        self.client_tree.heading('Prenom', text='Prenom', anchor=CENTER)
        self.client_tree.heading('Nom', text='Nom', anchor=CENTER)
        self.client_tree.heading('Marque', text='Marque', anchor=CENTER)
        self.client_tree.heading('Model', text='Model', anchor=CENTER)
        self.client_tree.heading('Type', text='Type', anchor=CENTER)
        self.client_tree.heading('Utiliser', text='Utiliser', anchor=CENTER)
        self.client_tree.heading('CPU', text='CPU', anchor=CENTER)
        self.client_tree.heading('Stockage', text='Stockage', anchor=CENTER)
        self.client_tree.heading('RAM', text='RAM', anchor=CENTER)
        self.client_tree.heading('Tel', text='Tel', anchor=CENTER)
        self.client_tree.heading('Date', text='Date', anchor=CENTER)
        
        self.client_tree.tag_configure('oddrow', background="#E8E8E8")
        self.client_tree.tag_configure('evenrow', background="#DFDFDF")
        
        client_database(self.client_tree)
        
        self.command_frame = customtkinter.CTkFrame(self.tabview.tab('Les Demandes'))
        self.command_frame.grid(row = 5, column = 3, rowspan = 2, columnspan = 4, pady = 10, sticky = 'nsew')
        
        self.ajouter_button = customtkinter.CTkButton(self.command_frame, text='Ajouter', font=customtkinter.CTkFont('arial', 15, 'bold'), command=ajouter_client)
        self.ajouter_button.grid(row = 0, column = 0, padx = 20, pady = 15)
        
        self.modifier_button = customtkinter.CTkButton(self.command_frame, text='Modifier', font=customtkinter.CTkFont('arial', 15, 'bold'), command=modifier_client)
        self.modifier_button.grid(row = 0, column = 1, padx = 20, pady = 15)
        
        self.initialiser_button = customtkinter.CTkButton(self.command_frame, text='Initialiser', font=customtkinter.CTkFont('arial', 15, 'bold'), command=vider_client_entry)
        self.initialiser_button.grid(row = 0, column = 2, padx = 20, pady = 15)
        
        self.ajouter_facture_button = customtkinter.CTkButton(self.command_frame, text='Ajouter Facture', font=customtkinter.CTkFont('arial', 15, 'bold'), command=ajouter_facture)
        self.ajouter_facture_button.grid(row = 0, column = 3, padx = 20, pady = 15)
        
        self.supprimer_button = customtkinter.CTkButton(self.command_frame, text='Supprimer', font=customtkinter.CTkFont('arial', 15, 'bold'), fg_color='red', hover_color='#8b0000', command= lambda: supprimer_client(self.client_tree))
        self.supprimer_button.grid(row = 1, column = 0, padx = 20, pady = 15)
        
        self.supprimer_quelque_button = customtkinter.CTkButton(self.command_frame, text='Supprimer quelque', font=customtkinter.CTkFont('arial', 15, 'bold'), fg_color='red', hover_color='#8b0000', command= lambda: supprimer_quelque_client(self.client_tree))
        self.supprimer_quelque_button.grid(row = 1, column = 1, padx = 20, pady = 15)
        
        self.supprimer_tous_button = customtkinter.CTkButton(self.command_frame, text='Supprimer Tous', font=customtkinter.CTkFont('arial', 15, 'bold'), fg_color='red', hover_color='#8b0000', command= lambda: supprimer_tous_client(self.client_tree))
        self.supprimer_tous_button.grid(row = 1, column = 2, padx = 20, pady = 15)
        
        self.recherche_frame = customtkinter.CTkFrame(self.tabview.tab('Les Demandes'), width=1130, height=50)
        self.recherche_frame.grid(row = 20, column = 0, columnspan = 8, pady = 10, sticky = 'nsew')
        
        self.recherche_entry = customtkinter.CTkEntry(self.recherche_frame, width=800, placeholder_text='...')
        self.recherche_entry.grid(row = 0, column = 0, columnspan = 6, pady = 20, sticky = 'nsew')
        
        self.recherche_button = customtkinter.CTkButton(self.recherche_frame, text='Rechercher', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: recherche_client(self.client_tree))
        self.recherche_button.grid(row = 0, column = 7, pady = 20, padx = 10,sticky = 'nsew')
        
        self.refraichir_button = customtkinter.CTkButton(self.recherche_frame, text='Refraichir', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: refraichir_client(self.client_tree))
        self.refraichir_button.grid(row = 0, column = 8, pady = 20, padx = 10, sticky = 'nsew')
    
        self.client_tree.bind('<ButtonRelease-1>', select_client)
        
        
    def destroy_client(self):
        
        for widget in window.winfo_children():
            widget.destroy()
    

class Stock:
    
    def __init__(self) -> None:
        
        self.menu = Menu()
        
        self.contenu_frame = customtkinter.CTkFrame(window, width=WIDTH, height=480)
        self.contenu_frame.grid(row = 1, column = 0, rowspan = 14, columnspan = 6, pady = 10, sticky = 'nsew')
        
        self.record_frame = customtkinter.CTkFrame(self.contenu_frame, width=380, height=380)
        self.record_frame.grid(row = 0, column = 0, rowspan = 11, pady = 10, sticky = 'nsew')
        
        self.o_code_lebel = customtkinter.CTkLabel(self.record_frame, text='Code:')
        self.o_code_lebel.grid(row = 0, column = 0, padx = 65)
        self.o_code_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_code_entry.grid(row = 1, column = 0, padx = 10, pady = 5)
        
        self.o_marque_lebel = customtkinter.CTkLabel(self.record_frame, text='Marque:')
        self.o_marque_lebel.grid(row = 0, column = 1, padx = 65)
        self.o_marque_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_marque_entry.grid(row = 1, column = 1, padx = 10, pady = 5)
        
        self.o_model_lebel = customtkinter.CTkLabel(self.record_frame, text='Model:')
        self.o_model_lebel.grid(row = 2, column = 0, padx = 65)
        self.o_model_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_model_entry.grid(row = 3, column = 0, padx = 10, pady = 5)
        
        self.o_type_lebel = customtkinter.CTkLabel(self.record_frame, text='Type:')
        self.o_type_lebel.grid(row = 2, column = 1, padx = 65)
        self.o_type_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_type_entry.grid(row = 3, column = 1, padx = 10, pady = 5)
        
        self.o_utiliser_lebel = customtkinter.CTkLabel(self.record_frame, text='Utiliser:')
        self.o_utiliser_lebel.grid(row = 4, column = 0, padx = 65)
        self.o_utiliser_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_utiliser_entry.grid(row = 5, column = 0, padx = 10, pady = 5)
        
        self.o_os_lebel = customtkinter.CTkLabel(self.record_frame, text='OS:')
        self.o_os_lebel.grid(row = 4, column = 1, padx = 65)
        self.o_os_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_os_entry.grid(row = 5, column = 1, padx = 10, pady = 5)
        
        self.o_cpu_lebel = customtkinter.CTkLabel(self.record_frame, text='CPU:')
        self.o_cpu_lebel.grid(row = 6, column = 0, padx = 65)
        self.o_cpu_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_cpu_entry.grid(row = 7, column = 0, padx = 10, pady = 5)
        
        self.o_gpu_lebel = customtkinter.CTkLabel(self.record_frame, text='GPU:')
        self.o_gpu_lebel.grid(row = 6, column = 1, padx = 65)
        self.o_gpu_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_gpu_entry.grid(row = 7, column = 1, padx = 10, pady = 5)
        
        self.o_stockage_lebel = customtkinter.CTkLabel(self.record_frame, text='Stockage:')
        self.o_stockage_lebel.grid(row = 8, column = 0, padx = 65)
        self.o_stockage_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_stockage_entry.grid(row = 9, column = 0, padx = 10, pady = 5)
        
        self.o_ram_lebel = customtkinter.CTkLabel(self.record_frame, text='RAM:')
        self.o_ram_lebel.grid(row = 8, column = 1, padx = 65)
        self.o_ram_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_ram_entry.grid(row = 9, column = 1, padx = 10, pady = 5)
        
        self.o_prix_achat_lebel = customtkinter.CTkLabel(self.record_frame, text="Prix d'achat:")
        self.o_prix_achat_lebel.grid(row = 10, column = 0, padx = 65)
        self.o_prix_achat_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_prix_achat_entry.grid(row = 11, column = 0, padx = 10, pady = 5)
        
        self.o_prix_vente_lebel = customtkinter.CTkLabel(self.record_frame, text='Prix de vente:')
        self.o_prix_vente_lebel.grid(row = 10, column = 1, padx = 65)
        self.o_prix_vente_entry = customtkinter.CTkEntry(self.record_frame, width=150, placeholder_text='...')
        self.o_prix_vente_entry.grid(row = 11, column = 1, padx = 10, pady = 5)
        
        self.tree_frame = customtkinter.CTkFrame(self.contenu_frame, width=750, height=180)
        self.tree_frame.grid(row = 0, column = 2, rowspan = 7, columnspan = 6, pady = 10, sticky = 'nsew')
        
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('treeview',
                background='#D3D3D3',
                foreground='black',
                rowheight=25,
                fieldbackground='#D3D3D3')
        self.style.map('treeview',
                background=[('selected', '#347083')])
        
        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        
        self.stock_tree = ttk.Treeview(self.tree_frame, yscrollcommand=self.tree_scroll, selectmode='extended', height=15)
        self.stock_tree.pack()
        
        self.tree_scroll.config(command=self.stock_tree.yview)
        self.stock_tree['columns'] = ('Code', 'Marque', 'Model', 'Type', 'Utiliser', 'OS', 'CPU', 'GPU', 'Stockage', 'RAM', 'Prix_achat', 'Prix_vente')
        
        self.stock_tree.column('#0', width=0, stretch=NO)
        self.stock_tree.column('Code', anchor=CENTER, width=60)
        self.stock_tree.column('Marque', anchor=CENTER, width=110)
        self.stock_tree.column('Model', anchor=CENTER, width=100)
        self.stock_tree.column('Type', anchor=CENTER, width=80)
        self.stock_tree.column('Utiliser', anchor=CENTER, width=70)
        self.stock_tree.column('OS', anchor=CENTER, width=80)
        self.stock_tree.column('CPU', anchor=CENTER, width=120)
        self.stock_tree.column('GPU', anchor=CENTER, width=100)
        self.stock_tree.column('Stockage', anchor=CENTER, width=80)
        self.stock_tree.column('RAM', anchor=CENTER, width=50)
        self.stock_tree.column('Prix_vente', anchor=CENTER, width=100)
        self.stock_tree.column('Prix_achat', anchor=CENTER, width=100)
        
        self.stock_tree.heading('#0', text='', anchor=W)
        self.stock_tree.heading('Code', text='Code', anchor=CENTER)
        self.stock_tree.heading('Marque', text='Marque', anchor=CENTER)
        self.stock_tree.heading('Model', text='Model', anchor=CENTER)
        self.stock_tree.heading('Type', text='Type', anchor=CENTER)
        self.stock_tree.heading('Utiliser', text='Utiliser', anchor=CENTER)
        self.stock_tree.heading('OS', text='OS', anchor=CENTER)
        self.stock_tree.heading('CPU', text='CPU', anchor=CENTER)
        self.stock_tree.heading('GPU', text='GPU', anchor=CENTER)
        self.stock_tree.heading('Stockage', text='Stockage', anchor=CENTER)
        self.stock_tree.heading('RAM', text='RAM', anchor=CENTER)
        self.stock_tree.heading('Prix_vente', text='Prix_vente', anchor=CENTER)
        self.stock_tree.heading('Prix_achat', text='Prix_achat', anchor=CENTER)
        
        self.stock_tree.tag_configure('oddrow', background="#E8E8E8")
        self.stock_tree.tag_configure('evenrow', background="#DFDFDF")
        
        stock_database(self.stock_tree)
        
        self.ajouter_button = customtkinter.CTkButton(self.contenu_frame, text='Ajouter', font=customtkinter.CTkFont('arial', 15, 'bold'), command=ajouter_stock)
        self.ajouter_button.grid(row = 7, column = 2, pady = 15, padx = 10)
        
        self.modifier_button = customtkinter.CTkButton(self.contenu_frame, text='Modifier', font=customtkinter.CTkFont('arial', 15, 'bold'), command=modifier_stock)
        self.modifier_button.grid(row = 7, column = 3, pady = 15, padx = 10)
        
        self.initialiser_button = customtkinter.CTkButton(self.contenu_frame, text='Initialiser', font=customtkinter.CTkFont('arial', 15, 'bold'), command=vider_stock_entry)
        self.initialiser_button.grid(row = 7, column = 4, pady = 15, padx = 10)
        
        self.supprimer_button = customtkinter.CTkButton(self.contenu_frame, text='Supprimer', font=customtkinter.CTkFont('arial', 15, 'bold'), fg_color='red', hover_color='#8b0000', command= lambda: supprimer_stock(self.stock_tree))
        self.supprimer_button.grid(row = 7, column = 5, pady = 15, padx = 10)
        
        self.supprimer_quelque_button = customtkinter.CTkButton(self.contenu_frame, text='Supprimer quelque', font=customtkinter.CTkFont('arial', 15, 'bold'), fg_color='red', hover_color='#8b0000', command= lambda: supprimer_quelque_stock(self.stock_tree))
        self.supprimer_quelque_button.grid(row = 8, column = 2, pady = 15, padx = 10)
        
        self.supprimer_tous_button = customtkinter.CTkButton(self.contenu_frame, text='Supprimer Tous', font=customtkinter.CTkFont('arial', 15, 'bold'), fg_color='red', hover_color='#8b0000', command= lambda: supprimer_tous_stock(self.stock_tree))
        self.supprimer_tous_button.grid(row = 8, column = 3, pady = 15, padx = 10)
        
        self.recherche_frame = customtkinter.CTkFrame(self.contenu_frame, width=1130, height=50)
        self.recherche_frame.grid(row = 20, column = 0, columnspan = 8, pady = 8, sticky = 'nsew')
        
        self.stock_recherche_entry = customtkinter.CTkEntry(self.recherche_frame , width=800, placeholder_text='...')
        self.stock_recherche_entry.grid(row = 0, column = 0, columnspan = 3, sticky = 'nsew')
        
        self.recherche_button = customtkinter.CTkButton(self.recherche_frame, text='Rechercher', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: recherche_stock(self.stock_tree))
        self.recherche_button.grid(row = 0, column = 3, padx = 10,sticky = 'nsew')
        
        self.refraichir_button = customtkinter.CTkButton(self.recherche_frame, text='Refraichir', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: refraichir_stock(self.stock_tree))
        self.refraichir_button.grid(row = 0, column = 4, padx = 10, sticky = 'nsew')
        
        self.stock_tree.bind('<ButtonRelease-1>', select_stock)
        
    
    def destroy_stock(self):
        
        for widget in window.winfo_children():
            widget.destroy()

   
class Facture:
    
    def __init__(self) -> None:
        
        self.menu = Menu()
        
        self.tabview = customtkinter.CTkTabview(window, width=WIDTH, height=480)
        self.tabview.grid(row = 1, column = 0, sticky = 'nsew')
        self.tabview.add('Payer Cash')
        self.tabview.add('Payer Versements')
        self.tabview.add('Bon Client')
        self.tabview.add('Mauvais Client')
        self.tabview.tab('Payer Cash').grid_columnconfigure(4, weight=1)
        
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('treeview',
                background='#D3D3D3',
                foreground='black',
                rowheight=25,
                fieldbackground='#D3D3D3')
        self.style.map('treeview',
                background=[('selected', '#347083')])
        
        self.treeview_frame = customtkinter.CTkFrame(self.tabview.tab('Payer Cash'))
        self.treeview_frame.grid(row = 0, column = 0, columnspan = 4, rowspan = 3, sticky = 'nsew')
        
        self.tree_scroll_cash = customtkinter.CTkScrollbar(self.treeview_frame, height=50)
        self.tree_scroll_cash.pack(side=RIGHT, fill=Y)
        
        self.payer_cash_tree = ttk.Treeview(self.treeview_frame, yscrollcommand=self.tree_scroll_cash.set, selectmode='extended', height=11)
        self.payer_cash_tree.pack()
        
        self.payer_cash_tree['columns'] = ('N', 'Prenom', 'Nom', 'CIN', 'Prix de vente', 'Tel', 'Date')
        
        self.payer_cash_tree.column('#0', width=0, stretch=NO)
        self.payer_cash_tree.column('N', anchor=CENTER, width=100)
        self.payer_cash_tree.column('Prenom', anchor=CENTER, width=150)
        self.payer_cash_tree.column('Nom', anchor=CENTER, width=150)
        self.payer_cash_tree.column('CIN', anchor=CENTER, width=140)
        self.payer_cash_tree.column('Prix de vente', anchor=CENTER, width=120)
        self.payer_cash_tree.column('Tel', anchor=CENTER, width=180)
        self.payer_cash_tree.column('Date', anchor=CENTER, width=120)
        
        self.payer_cash_tree.heading('N', text='N', anchor=CENTER)
        self.payer_cash_tree.heading('Prenom', text='Prenom', anchor=CENTER)
        self.payer_cash_tree.heading('Nom', text='Nom', anchor=CENTER)
        self.payer_cash_tree.heading('CIN', text='CIN', anchor=CENTER)
        self.payer_cash_tree.heading('Prix de vente', text='Prix de vente', anchor=CENTER)
        self.payer_cash_tree.heading('Tel', text='Tel', anchor=CENTER)
        self.payer_cash_tree.heading('Date', text='Date', anchor=CENTER)
        
        self.payer_cash_tree.tag_configure('oddrow', background="#E8E8E8")
        self.payer_cash_tree.tag_configure('evenrow', background="#DFDFDF")
        
        cash_database(self.payer_cash_tree)
        
        self.record_frame = customtkinter.CTkFrame(self.tabview.tab('Payer Cash'))
        self.record_frame.grid(row = 4, column = 0, rowspan = 4, columnspan = 4, pady = 20, sticky = 'nsew')
        
        self.nFacture_label_cash = customtkinter.CTkLabel(self.record_frame, text="Numero de Facture")
        self.nFacture_label_cash.grid(row=0, column=0, padx=10, pady=20)
        self.nFacture_entry_cash = customtkinter.CTkEntry(self.record_frame, height=25, border_width=2, corner_radius=10, placeholder_text='...')
        self.nFacture_entry_cash.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
        self.ouvrir_button = customtkinter.CTkButton(self.record_frame, text='ouvrir', font=customtkinter.CTkFont(family='arial', size = 15, weight='bold'), command=ouvrir_cash)
        self.ouvrir_button.grid(row = 1, column = 0)
        
        self.supprimer_tous_button = customtkinter.CTkButton(self.record_frame, text='supprimer tous', font=customtkinter.CTkFont(family='arial', size = 15, weight='bold'), fg_color='red', hover_color='#8b0000', command= lambda: supprimer_tous_cash(self.payer_cash_tree))
        self.supprimer_tous_button.grid(row = 1, column = 4)
        
        self.recherche_cash_entry = customtkinter.CTkEntry(self.record_frame, width=400, placeholder_text='...')
        self.recherche_cash_entry.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 110, sticky = 'nsew')
        
        self.recherche_button = customtkinter.CTkButton(self.record_frame, text='Rechercher', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: rechercher_cash(self.payer_cash_tree))
        self.recherche_button.grid(row = 2, column = 3, padx = 5, pady = 110, sticky = 'nsew')
        
        self.refraichir_button = customtkinter.CTkButton(self.record_frame, text='Refraichir', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: refraichir_cash(self.payer_cash_tree))
        self.refraichir_button.grid(row = 2, column = 4, padx = 5, pady = 110, sticky = 'nsew')
        
        self.tree_scroll_cash.configure(self.payer_cash_tree.yview)
        self.payer_cash_tree.bind('<ButtonRelease-1>', select_cash)
        
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('treeview',
                background='#D3D3D3',
                foreground='black',
                rowheight=25,
                fieldbackground='#D3D3D3')
        self.style.map('treeview',
                background=[('selected', '#347083')])
        
        self.treeview_frame = customtkinter.CTkFrame(self.tabview.tab('Payer Versements'))
        self.treeview_frame.grid(row = 0, column = 0, columnspan = 4, rowspan = 3, sticky = 'nsew')
        
        self.tree_scroll = customtkinter.CTkScrollbar(self.treeview_frame, height=50)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        
        self.payer_versements_tree = ttk.Treeview(self.treeview_frame, yscrollcommand=self.tree_scroll.set, selectmode='extended', height=11)
        self.payer_versements_tree.pack()
        
        self.payer_versements_tree['columns'] = ('N', 'Prenom', 'Nom', 'CIN', 'Prix de vente', 'Avance', 'Tel', 'Date de depart')
        
        self.payer_versements_tree.column('#0', width=0, stretch=NO)
        self.payer_versements_tree.column('N', anchor=CENTER, width=70)
        self.payer_versements_tree.column('Prenom', anchor=CENTER, width=130)
        self.payer_versements_tree.column('Nom', anchor=CENTER, width=130)
        self.payer_versements_tree.column('CIN', anchor=CENTER, width=110)
        self.payer_versements_tree.column('Prix de vente', anchor=CENTER, width=120)
        self.payer_versements_tree.column('Avance', anchor=CENTER, width=100)
        self.payer_versements_tree.column('Tel', anchor=CENTER, width=160)
        self.payer_versements_tree.column("Date de depart", anchor=CENTER, width=130)
        
        self.payer_versements_tree.heading('N', text='N', anchor=CENTER)
        self.payer_versements_tree.heading('Prenom', text='Prenom', anchor=CENTER)
        self.payer_versements_tree.heading('Nom', text='Nom', anchor=CENTER)
        self.payer_versements_tree.heading('CIN', text='CIN', anchor=CENTER)
        self.payer_versements_tree.heading('Prix de vente', text='Prix de vente', anchor=CENTER)
        self.payer_versements_tree.heading('Avance', text='Avance', anchor=CENTER)
        self.payer_versements_tree.heading('Tel', text='Tel', anchor=CENTER)
        self.payer_versements_tree.heading('Date de depart', text='Date de depart', anchor=CENTER)
        
        self.payer_versements_tree.tag_configure('oddrow', background="#E8E8E8")
        self.payer_versements_tree.tag_configure('evenrow', background="#DFDFDF")
        
        versement_database(self.payer_versements_tree)
        
        self.record_frame = customtkinter.CTkFrame(self.tabview.tab('Payer Versements'))
        self.record_frame.grid(row = 4, column = 0, rowspan = 4, columnspan = 4, pady = 20, sticky = 'nsew')
        
        self.nFacture_label_versement = customtkinter.CTkLabel(self.record_frame, text="Numero de Facture")
        self.nFacture_label_versement.grid(row=0, column=0, padx=10, pady=20)
        self.nFacture_entry_versement = customtkinter.CTkEntry(self.record_frame, height=25, border_width=2, corner_radius=10, placeholder_text='...')
        self.nFacture_entry_versement.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
        self.avance_label_versement = customtkinter.CTkLabel(self.record_frame, text="Avance")
        self.avance_label_versement.grid(row=1, column=0, padx=10, pady=20)
        self.avance_entry_versement = customtkinter.CTkEntry(self.record_frame, height=25, border_width=2, corner_radius=10, placeholder_text='...')
        self.avance_entry_versement.grid(row=1, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
        self.payer_button = customtkinter.CTkButton(self.record_frame, text='payer', font=customtkinter.CTkFont(family='arial', size = 15, weight='bold'), command= lambda: modifier_avance(self.payer_versements_tree))
        self.payer_button.grid(row = 1, column = 3)
        
        self.ouvrir_button = customtkinter.CTkButton(self.record_frame, text='ouvrir', font=customtkinter.CTkFont(family='arial', size = 15, weight='bold'), command=ouvrir_versement)
        self.ouvrir_button.grid(row = 2, column = 0)
        
        self.supprimer_tous_button = customtkinter.CTkButton(self.record_frame, text='supprimer tous', font=customtkinter.CTkFont(family='arial', size = 15, weight='bold'), fg_color='red', hover_color='#8b0000', command= lambda: supprimer_tous_versement(self.payer_versements_tree))
        self.supprimer_tous_button.grid(row = 2, column = 4)
        
        self.versement_recherche_entry = customtkinter.CTkEntry(self.record_frame, width=400, placeholder_text='...')
        self.versement_recherche_entry.grid(row = 3, column = 0, columnspan = 2, padx = 5, pady = 40, sticky = 'nsew')
        
        self.recherche_button = customtkinter.CTkButton(self.record_frame, text='Rechercher', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: rechercher_versement(self.payer_versements_tree))
        self.recherche_button.grid(row = 3, column = 3, padx = 5, pady = 40, sticky = 'nsew')
        
        self.refraichir_button = customtkinter.CTkButton(self.record_frame, text='Refraichir', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: refraichir_versement(self.payer_versements_tree))
        self.refraichir_button.grid(row = 3, column = 4, padx = 5, pady = 40, sticky = 'nsew')
        
        self.payer_versements_tree.bind('<ButtonRelease-1>', select_versement)
        
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('treeview',
                background='#D3D3D3',
                foreground='black',
                rowheight=25,
                fieldbackground='#D3D3D3')
        self.style.map('treeview',
                background=[('selected', '#347083')])
        
        self.treeview_frame = customtkinter.CTkFrame(self.tabview.tab('Bon Client'))
        self.treeview_frame.grid(row = 0, column = 0, columnspan = 4, rowspan = 3, sticky = 'nsew')
        
        self.tree_scroll = customtkinter.CTkScrollbar(self.treeview_frame, height=50)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        
        self.bon_client_tree = ttk.Treeview(self.treeview_frame, yscrollcommand=self.tree_scroll.set, selectmode='extended', height=11)
        self.bon_client_tree.pack()
        
        self.bon_client_tree['columns'] = ('N', 'Prenom', 'Nom', 'CIN', 'Prix de vente', 'Tel', 'Date')
        
        self.bon_client_tree.column('#0', width=0, stretch=NO)
        self.bon_client_tree.column('N', anchor=CENTER, width=100)
        self.bon_client_tree.column('Prenom', anchor=CENTER, width=150)
        self.bon_client_tree.column('Nom', anchor=CENTER, width=150)
        self.bon_client_tree.column('CIN', anchor=CENTER, width=140)
        self.bon_client_tree.column('Prix de vente', anchor=CENTER, width=120)
        self.bon_client_tree.column('Tel', anchor=CENTER, width=180)
        self.bon_client_tree.column('Date', anchor=CENTER, width=130)
        
        self.bon_client_tree.heading('N', text='N', anchor=CENTER)
        self.bon_client_tree.heading('Prenom', text='Prenom', anchor=CENTER)
        self.bon_client_tree.heading('Nom', text='Nom', anchor=CENTER)
        self.bon_client_tree.heading('CIN', text='CIN', anchor=CENTER)
        self.bon_client_tree.heading('Prix de vente', text='Prix de vente', anchor=CENTER)
        self.bon_client_tree.heading('Tel', text='Tel', anchor=CENTER)
        self.bon_client_tree.heading('Date', text='Date', anchor=CENTER)
        
        self.bon_client_tree.tag_configure('oddrow', background="#E8E8E8")
        self.bon_client_tree.tag_configure('evenrow', background="#DFDFDF")
        
        bon_database(self.bon_client_tree)
        
        self.record_frame = customtkinter.CTkFrame(self.tabview.tab('Bon Client'))
        self.record_frame.grid(row = 4, column = 0, rowspan = 4, columnspan = 4, pady = 20, sticky = 'nsew')
        
        self.nFacture_label = customtkinter.CTkLabel(self.record_frame, text="Numero de Facture")
        self.nFacture_label.grid(row=0, column=0, padx=10, pady=20)
        self.bon_nFacture_entry = customtkinter.CTkEntry(self.record_frame, height=25, border_width=2, corner_radius=10, placeholder_text='...')
        self.bon_nFacture_entry.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
        self.ouvrir_button = customtkinter.CTkButton(self.record_frame, text='ouvrir', font=customtkinter.CTkFont(family='arial', size = 15, weight='bold'), command=ouvrir_bon)
        self.ouvrir_button.grid(row = 1, column = 0)
        
        self.supprimer_tous_button = customtkinter.CTkButton(self.record_frame, text='supprimer tous', font=customtkinter.CTkFont(family='arial', size = 15, weight='bold'), fg_color='red', hover_color='#8b0000', command= lambda: supprimer_tous_bon(self.bon_client_tree))
        self.supprimer_tous_button.grid(row = 1, column = 4)
        
        self.bon_recherche_entry = customtkinter.CTkEntry(self.record_frame, width=400, placeholder_text='...')
        self.bon_recherche_entry.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 110, sticky = 'nsew')
        
        self.recherche_button = customtkinter.CTkButton(self.record_frame, text='Rechercher', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: rechercher_bon(self.bon_client_tree))
        self.recherche_button.grid(row = 2, column = 3, padx = 5, pady = 110, sticky = 'nsew')
        
        self.refraichir_button = customtkinter.CTkButton(self.record_frame, text='Refraichir', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: refraichir_bon(self.bon_client_tree))
        self.refraichir_button.grid(row = 2, column = 4, padx = 5, pady = 110, sticky = 'nsew')
        
        self.bon_client_tree.bind('<ButtonRelease-1>', select_bon)
        
        self.style = ttk.Style()
        self.style.theme_use('default')
        self.style.configure('treeview',
                background='#D3D3D3',
                foreground='black',
                rowheight=25,
                fieldbackground='#D3D3D3')
        self.style.map('treeview',
                background=[('selected', '#347083')])
        
        self.treeview_frame = customtkinter.CTkFrame(self.tabview.tab('Mauvais Client'))
        self.treeview_frame.grid(row = 0, column = 0, columnspan = 4, rowspan = 3, sticky = 'nsew')
        
        self.tree_scroll = customtkinter.CTkScrollbar(self.treeview_frame, height=50)
        self.tree_scroll.pack(side=RIGHT, fill=Y)
        
        self.mauvais_client_tree = ttk.Treeview(self.treeview_frame, yscrollcommand=self.tree_scroll.set, selectmode='extended', height=11)
        self.mauvais_client_tree.pack()
        
        self.mauvais_client_tree['columns'] = ('N', 'Prenom', 'Nom', 'CIN', 'Prix non payer', 'Tel', 'Date')
        
        self.mauvais_client_tree.column('#0', width=0, stretch=NO)
        self.mauvais_client_tree.column('N', anchor=CENTER, width=100)
        self.mauvais_client_tree.column('Prenom', anchor=CENTER, width=150)
        self.mauvais_client_tree.column('Nom', anchor=CENTER, width=150)
        self.mauvais_client_tree.column('CIN', anchor=CENTER, width=140)
        self.mauvais_client_tree.column('Prix non payer', anchor=CENTER, width=120)
        self.mauvais_client_tree.column('Tel', anchor=CENTER, width=180)
        self.mauvais_client_tree.column('Date', anchor=CENTER, width=130)
        
        self.mauvais_client_tree.heading('N', text='N', anchor=CENTER)
        self.mauvais_client_tree.heading('Prenom', text='Prenom', anchor=CENTER)
        self.mauvais_client_tree.heading('Nom', text='Nom', anchor=CENTER)
        self.mauvais_client_tree.heading('CIN', text='CIN', anchor=CENTER)
        self.mauvais_client_tree.heading('Prix non payer', text='Prix non payer', anchor=CENTER)
        self.mauvais_client_tree.heading('Tel', text='Tel', anchor=CENTER)
        self.mauvais_client_tree.heading('Date', text='Date', anchor=CENTER)
        
        self.mauvais_client_tree.tag_configure('oddrow', background="#E8E8E8")
        self.mauvais_client_tree.tag_configure('evenrow', background="#DFDFDF")
        
        mauvais_database(self.mauvais_client_tree)
        
        self.record_frame = customtkinter.CTkFrame(self.tabview.tab('Mauvais Client'))
        self.record_frame.grid(row = 4, column = 0, rowspan = 4, columnspan = 4, pady = 20, sticky = 'nsew')
        
        self.nFacture_label = customtkinter.CTkLabel(self.record_frame, text="Numero de Facture")
        self.nFacture_label.grid(row=0, column=0, padx=10, pady=20)
        self.mauvais_nFacture_entry = customtkinter.CTkEntry(self.record_frame, height=25, border_width=2, corner_radius=10, placeholder_text='...')
        self.mauvais_nFacture_entry.grid(row=0, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")
        
        self.ouvrir_button = customtkinter.CTkButton(self.record_frame, text='ouvrir', font=customtkinter.CTkFont(family='arial', size = 15, weight='bold'), command=ouvrir_mauvais)
        self.ouvrir_button.grid(row = 1, column = 0)
        
        self.supprimer_tous_button = customtkinter.CTkButton(self.record_frame, text='supprimer tous', font=customtkinter.CTkFont(family='arial', size = 15, weight='bold'), fg_color='red', hover_color='#8b0000', command= lambda: supprimer_tous_mauvais(self.mauvais_client_tree))
        self.supprimer_tous_button.grid(row = 1, column = 4)
        
        self.mauvais_recherche_entry = customtkinter.CTkEntry(self.record_frame, width=400, placeholder_text='...')
        self.mauvais_recherche_entry.grid(row = 2, column = 0, columnspan = 2, padx = 5, pady = 110, sticky = 'nsew')
        
        self.recherche_button = customtkinter.CTkButton(self.record_frame, text='Rechercher', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: rechercher_mauvais(self.mauvais_client_tree))
        self.recherche_button.grid(row = 2, column = 3, padx = 5, pady = 110, sticky = 'nsew')
        
        self.refraichir_button = customtkinter.CTkButton(self.record_frame, text='Refraichir', fg_color='transparent', font=customtkinter.CTkFont('arial', 15, 'bold'), text_color=("gray10", "#DCE4EE"), border_width=2, command= lambda: refraichir_mauvais(self.mauvais_client_tree))
        self.refraichir_button.grid(row = 2, column = 4, padx = 5, pady = 110, sticky = 'nsew')
        
        self.mauvais_client_tree.bind('<ButtonRelease-1>', select_mauvais)
        
    
    def destroy_facture(self):
        
        for widget in window.winfo_children():
            widget.destroy()
            
        
class client_bill:
    
    def __init__(self) -> None:

        self.menu = Menu()
        
        self.contenu_frame = customtkinter.CTkFrame(window)
        self.contenu_frame.grid(row = 1, column = 0, rowspan = 4, columnspan = 3, sticky = 'nsew')
        
        self.cin_box = simpledialog.askstring('CIN', 'Donnez votre CIN.\t\t\t\t', parent=self.contenu_frame)
        
        self.appareil_label = customtkinter.CTkLabel(self.contenu_frame, text='Appareil:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.appareil_label.grid(row = 0, column = 0, padx = 50, pady = 20)
        self.appareil_entry = customtkinter.CTkEntry(self.contenu_frame, width=300, placeholder_text='...')
        self.appareil_entry.grid(row = 0, column = 1, padx = 50, pady = 20)
        
        self.prix_label = customtkinter.CTkLabel(self.contenu_frame, text='Prix:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.prix_label.grid(row = 1, column = 0, padx = 50, pady = 20)
        self.prix_entry = customtkinter.CTkEntry(self.contenu_frame, width=300, placeholder_text='...')
        self.prix_entry.grid(row = 1, column = 1, padx = 50, pady = 20)
        
        self.quantite_label = customtkinter.CTkLabel(self.contenu_frame, text='Quantite:', font=customtkinter.CTkFont('arial', 15, 'bold'))
        self.quantite_label.grid(row = 2, column = 0, padx = 50, pady = 20)
        self.quantite_entry = customtkinter.CTkEntry(self.contenu_frame, width=300, placeholder_text='...')
        self.quantite_entry.grid(row = 2, column = 1, padx = 50, pady = 20)
        
        self.ajouter_button = customtkinter.CTkButton(self.contenu_frame, text='Ajouter', font=customtkinter.CTkFont('arial', 15, 'bold'), command = ajouter_au_facture)
        self.ajouter_button.grid(row = 4, column = 0, padx = 30, pady = 20)
        
        self.initialiser_button = customtkinter.CTkButton(self.contenu_frame, text='Initialiser', font=customtkinter.CTkFont('arial', 15, 'bold'), command = vider_bill)
        self.initialiser_button.grid(row = 4, column = 1, padx = 30, pady = 20, sticky = 'w')
        
        self.souvegarder_button = customtkinter.CTkButton(self.contenu_frame, text='Souvegarder', font=customtkinter.CTkFont('arial', 15, 'bold'), command = souvegarder)
        self.souvegarder_button.grid(row = 5, column = 0, padx = 30, pady = 20)

        self.bill = tkst.ScrolledText(self.contenu_frame, bg='white', wrap = WORD)
        self.bill.grid(row = 0, column = 3, rowspan = 8, padx = 20, pady = 20)
        
        
    def destroy_client_bill(self):
        
        for widget in window.winfo_children():
            widget.destroy()
        
        
class cash_bill:
    
    def __init__(self) -> None:
        
        self.menu = Menu()
        
        self.contenu_frame = customtkinter.CTkFrame(window)
        self.contenu_frame.grid(row = 1, column = 0, rowspan = 10, columnspan = 10, sticky = 'nsew')
        
        self.cash_bill = tkst.ScrolledText(self.contenu_frame, bg='white', wrap = WORD)
        self.cash_bill.grid(row = 1, column = 1, columnspan = 5, rowspan = 8, padx = 500, pady = 100, sticky='nsew')
        
        self.cash_fermer_button = customtkinter.CTkButton(self.contenu_frame, text='fermer', font=customtkinter.CTkFont('arial', 15, 'bold'), command=fermer_cash)
        self.cash_fermer_button.grid(row = 9, column = 3, pady = 10, sticky = 's')
        
        
    def destroy_cash_bill(self):
        
        for widget in window.winfo_children():
            widget.destroy()
            
            
class versement_bill:
    
    def __init__(self) -> None:
        
        self.menu = Menu()
        
        self.contenu_frame = customtkinter.CTkFrame(window)
        self.contenu_frame.grid(row = 1, column = 0, rowspan = 18, columnspan = 10, sticky = 'nsew')
        
        self.versement_bill = tkst.ScrolledText(self.contenu_frame, bg='white', wrap = WORD)
        self.versement_bill.grid(row = 1, column = 1, columnspan = 11, rowspan = 8, padx = 500, pady = 100, sticky='nsew')
        
        self.versement_bon_button = customtkinter.CTkButton(self.contenu_frame, text='Bon Client', font=customtkinter.CTkFont('arial', 15, 'bold'), command= ajouter_bon)
        self.versement_bon_button.grid(row = 8, column = 5)
        
        self.versement_mauvais_button = customtkinter.CTkButton(self.contenu_frame, text='Mauvais Client', font=customtkinter.CTkFont('arial', 15, 'bold'), command=ajouter_mauvais)
        self.versement_mauvais_button.grid(row = 8, column = 6)
        
        self.versement_fermer_button = customtkinter.CTkButton(self.contenu_frame, text='fermer', font=customtkinter.CTkFont('arial', 15, 'bold'), command=fermer_versement)
        self.versement_fermer_button.grid(row = 8, column = 7)
        
        
    def destroy_versement_bill(self):
        
        for widget in window.winfo_children():
            widget.destroy()
            
            
class bon_bill:
    
    def __init__(self) -> None:
        
        self.menu = Menu()
        
        self.contenu_frame = customtkinter.CTkFrame(window)
        self.contenu_frame.grid(row = 1, column = 0, rowspan = 10, columnspan = 10, sticky = 'nsew')
        
        self.bon_bill = tkst.ScrolledText(self.contenu_frame, bg='white', wrap = WORD)
        self.bon_bill.grid(row = 1, column = 1, columnspan = 5, rowspan = 8, padx = 500, pady = 100, sticky='nsew')
        
        self.bon_fermer_button = customtkinter.CTkButton(self.contenu_frame, text='fermer', font=customtkinter.CTkFont('arial', 15, 'bold'), command=fermer_bon)
        self.bon_fermer_button.grid(row = 9, column = 3, pady = 10, sticky = 's')
        
        
    def destroy_bon_bill(self):
        
        for widget in window.winfo_children():
            widget.destroy()
            
            
class mauvais_bill:
    
    def __init__(self) -> None:
        
        self.menu = Menu()
        
        self.contenu_frame = customtkinter.CTkFrame(window)
        self.contenu_frame.grid(row = 1, column = 0, rowspan = 10, columnspan = 10, sticky = 'nsew')
        
        self.mauvais_bill = tkst.ScrolledText(self.contenu_frame, bg='white', wrap = WORD)
        self.mauvais_bill.grid(row = 1, column = 1, columnspan = 5, rowspan = 8, padx = 500, pady = 100, sticky='nsew')
        
        self.mauvais_fermer_button = customtkinter.CTkButton(self.contenu_frame, text='fermer', font=customtkinter.CTkFont('arial', 15, 'bold'), command=fermer_mauvais)
        self.mauvais_fermer_button.grid(row = 9, column = 3, pady = 10, sticky = 's')
        
        
    def destroy_mauvais_bill(self):
        
        for widget in window.winfo_children():
            widget.destroy()


global_frame = Accueil()
window.mainloop()