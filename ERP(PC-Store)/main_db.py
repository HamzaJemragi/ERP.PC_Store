import sqlite3

# database
# Client db
def client_db():
    
    client_db = sqlite3.connect('H_Client.db')
    client_cursor = client_db.cursor()
    client_cursor.execute('CREATE TABLE if not exists Client(prenom, nom, marque, model, type, utiliser, cpu, stockage, ram, tel, date)')
    client_db.commit()
    client_db.close()
    

# Stock db
def stock_db():
    
    stock_db = sqlite3.connect('Stock.db')
    stock_cursor = stock_db.cursor()
    stock_cursor.execute('CREATE TABLE if not exists Stock(code, marque, model, type, utiliser, os, cpu, gpu, stockage, ram, prix_achat, prix_vente)')
    stock_db.commit()
    stock_db.close()
    

# Facture Cash db
def facture_cash_db():
    
    facture_cash_db = sqlite3.connect('Facture_Cash.db')
    facture_cash_cursor = facture_cash_db.cursor()
    facture_cash_cursor.execute('CREATE TABLE if not exists Cash(numero, prenom, nom, cin, prix_vente, tel, date)')
    facture_cash_db.commit()
    facture_cash_db.close()


# Facture versement db
def facture_versement_db():
    
    facture_versement_db = sqlite3.connect('Facture_Versement.db')
    facture_versement_cursor = facture_versement_db.cursor()
    facture_versement_cursor.execute('CREATE TABLE if not exists Versement(numero, prenom, nom, cin, prix_vente, avance, tel, date_depart)')
    facture_versement_db.commit()
    facture_versement_db.close()
    

# Bon Client db
def bon_client_db():
    
    bon_client_db = sqlite3.connect('Bon_Client.db')
    bon_client_cursor = bon_client_db.cursor()
    bon_client_cursor.execute('CREATE TABLE if not exists Bon(numero, prenom, nom, cin, prix_vente, tel, date)')
    bon_client_db.commit()
    bon_client_db.close()
    

# Mauvais Client db
def mauvais_client_db():
    
    mauvais_client_db = sqlite3.connect('Mauvais_Client.db')
    mauvais_client_cursor = mauvais_client_db.cursor()
    mauvais_client_cursor.execute('CREATE TABLE if not exists Mauvais(numero, prenom, nom, cin, prix_non_payer, tel, date)')
    mauvais_client_db.commit()
    mauvais_client_db.close()