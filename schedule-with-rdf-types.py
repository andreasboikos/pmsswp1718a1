
# coding: utf-8

# # Μετατρέποντας στη μορφή N-Triples
# 
# Ολοκληρώνουμε την κατασκευή του ωρολογίου προγράμματος, μετατρέποντας τις τριάδες στο πρότυπο μορφότυπο [N-Triples](http://www.w3.org/TR/n-triples/).
# 
# ## 1. Φορτώστε τις τριάδες
# 
# Βάλτε σε μια λίστα τις τριάδες από το τελικό csv του προηγούμενου εργαστηρίου. Αυτές θα πρέπει:
# 
# * Να χρησιμοποιούν URIs με νόμιμους χαρακτήρες
# * Να έχουν σημειωμένους τους ανώνυμους κόμβους με το πρόθεμα `_:`
# * Όλα τα URIs να έχουν τη μορφή http URIs
# 
#     * `http://dilab77.ionio.gr/swp/you/vocab#` για τα κατηγορήματα
#     * `http://dilab77.ionio.gr/swp/you/resource/` για τα υπόλοιπα URIs
#     
#     όπου you πρέπει να είναι το username που έχετε στο JupyterHub.
#    

# In[44]:

import csv

ntriples=[]
with open('urilist.csv','r',newline='') as ifp:
    reader=csv.reader(ifp)
    
    for nt in reader:
        ntriples.append(nt)
    print(ntriples)


# ## 2. Καθορίστε τους τύπους δεδομένων
# 
# Οι απλές τιμές (literals) πρέπει να μετατραπούν σε **έγκυρη σύνταξη N-Triples**. Μέσω της Python
# 
# * Εκφράστε τις ημέρες και το εξάμηνο σε απλά strings (π.χ. `"Δευτέρα"`).
# * Μετατρέψτε τις ώρες στο τύπο `xsd:time`.
# * Όλα τα URIs πρέπει να είναι μέσα σε `< >`.
# 
# Ανατρέξτε στις διαφάνειες της τρέχουσας ενότητας για τη σωστή σύνταξη των προηγούμενων!
# 
# **Σημείωση:** Ο τύπος `xsd:time` **πρέπει υποχρεωτικά** να έχει τη μορφή (ώρα, λεπτά, δευτερόλεπτα), π.χ. `"18:00:00"^^<http://www.w3.org/2001/XMLSchema#time>`.

# In[156]:

newtriples = []
with open('schedule-data.nt','w') as ofp:
    for s,p,o in ntriples:
        p='<' + p + '>'
        if p=='<http://dilab77.ionio.gr/swp/c17boik/vocab#Ημέρα>':
            o='"' + o + '"'
            ofp.write('{} {} {}.\n'.format(s,p,o,s+p+o))
        if o.startswith('http'):
            o='<' + o + '>'
            ofp.write('{} {} {}.\n'.format(s,p,o,s+p+o))
        if p=='<http://dilab77.ionio.gr/swp/c17boik/vocab#Έναρξη>' or p=='<http://dilab77.ionio.gr/swp/c17boik/vocab#Λήξη>':
            o=o + ':00'
            o='"'+ o + '"' + '^^<http://www.w3.org/2001/XMLSchema#time>'
            ofp.write('{} {} {}.\n'.format(s,p,o,s+p+o))
        if s=='<http://dilab77.ionio.gr/swp/c17boik/vocab#Αίθουσα>':
            print('{} {} {} . \n'.format(o,'<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>','<http://dilab77.ionio.gr/swp/c17boik/vocab#Teacher>'))
            ofp.write('{} {} {} . \n'.format(o,'<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>','<http://dilab77.ionio.gr/swp/c17boik/vocab#Teacher>'))
        if p=='<http://dilab77.ionio.gr/swp/c17boik/vocab#Καθηγητής>':
            print('{} {} {} . \n'.format(o,'<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>','<http://dilab77.ionio.gr/swp/c17boik/vocab#Teacher>'))
            ofp.write('{} {} {} . \n'.format(o,'<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>','<http://dilab77.ionio.gr/swp/c17boik/vocab#Teacher>'))
        if p=='<http://dilab77.ionio.gr/swp/c17boik/vocab#Μάθημα>':
            print('{} {} {} . \n'.format(o,'<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>','<http://dilab77.ionio.gr/swp/c17boik/vocab#Course>'))
            ofp.write('{} {} {} . \n'.format(o,'<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>','<http://dilab77.ionio.gr/swp/c17boik/vocab#Course>'))
        if p=='<http://dilab77.ionio.gr/swp/c17boik/vocab#Αίθουσα>':
            print('{} {} {} . \n'.format(o,'<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>','<http://dilab77.ionio.gr/swp/c17boik/vocab#Class>'))
            print('{} {} {} . \n'.format(s,'<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>','<http://dilab77.ionio.gr/swp/c17boik/vocab#Lecture>'))
            ofp.write('{} {} {} . \n'.format(o,'<http://www.w3.org/1999/02/22-rdf-syntax-ns#type>','<http://dilab77.ionio.gr/swp/c17boik/vocab#Class>'))
           
            
    newtriples.append((s,p,o))
print(newtriples)

       

    


# ## 3. Παραγωγή αρχείου N-triples
# 
# Στο τελευταίο αυτό βήμα, αποθηκεύστε το περιεχόμενο των τριάδων σε αρχείο κειμένου σύμφωνα με το πρότυπο N-Triples. Το αρχείο σας θα πρέπει να έχει κατάληξη `.nt` .
# 
# **Θυμηθείτε**: κάθε γραμμή ενός αρχείου N-Triples περιέχει **ακριβώς μία** τριάδα, με τα μέρη των τριάδων χωρισμένα με κενό (space). Η γραμμή τελειώνει με την **τελεία**.

# #### Υποδειξη: μορφοποίηση strings
# 
# Μια απλή μορφοποίηση ενός string μπορεί να γίνει ως εξής
# 
# ```python
# a = 1
# b = 2
# print('{}+{}={}'.format(a,b,a+b))
# ```
# 
# Χρησιμοποιήστε τη `format()` όπως στο παράδειγμα για να φτιάξετε κάθε γραμμή του αρχείου N-Triples. Όταν φτάσετε στο επιθυμητό αποτέλεσμα, αντικαταστήστε την `print()` με τη μέθοδο `write()` του αρχείου εξόδου. Προσοχή: η `write()` δεν προσθέτει αυτόματα χαρακτήρα νέας γραμμής `\n`, πρέπει να τον βάλετε εσείς!

# In[ ]:


       


# ## 4. Είναι το αρχείο σας έγκυρο;
# 
# Βεβαιωθείτε ότι το αρχείο σας έχει έγκυρη μορφή N-Triples. Αυτό θα το κάνετε μέσω του εργαλείου `riot`. Στο επόμενο κελί εισάγετε το εξής:
# 
# `!riot --validate yourfile.nt`
# 
# Περιμένετε μέχρι να ολοκληρωθεί η εκτέλεση (να μην φαίνεται `In [*]`). **Αν το αρχείο σας είναι ΟΚ, δεν θα δείτε τίποτα ως έξοδο!**

# In[1]:

get_ipython().system('riot --validate schedule-data.nt')


# ## 5. Δεδομένα RDF σε άλλες μορφές.
# 
# Εφόσον έχετε έγκυρο αρχείο N-Triples, μπορείτε να το μετατρέψετε σε διάφορες άλλες μορφές. Το εργαλείο `riot` θα σας βοηθήσει πάλι:
# 
# Δοκιμάστε την εντολή `!riot --output=FMT yourfile.nt`, βάζοντας στη θέση του `FMT` τα `turtle` και `rdfxml`. Η έξοδος θα φανεί στην οθόνη σας.
# 
# Αν θέλετε να σώσετε σε νέο αρχείο την καινούργια μορφή, δώστε π.χ.:
# 
# `!riot --output=turtle yourfile.nt > yourfile.ttl`

# In[ ]:




# In[ ]:




# ## Το τέλος του ωρολογίου προγράμματος.
# 
# **Συγχαρητήρια!!** Μόλις περάσατε από τα ad hoc σημασιολογικά δεδομένα σε πρότυπες μορφές αναπαράστασης. Τώρα πλέον μπορείτε να επεξεργαστείτε τα δεδομένα σας με όλα τα διαθέσιμα εργαλεία του Σημασιολογικού Ιστού!
