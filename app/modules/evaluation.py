filename = "data/reuters/cats.txt"
verdaderos=[]
true_positives=0
false_negatives=0
def evaluate(query,all_titles,predicted):
    global true_positives, false_negatives
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('training') and query in line:
                # Extraer el número después del primer '/'
                number = line.split('/')[1].strip().split()[0]
                verdaderos.append(number)
    all_titles=all_titles
    obteing_true_positives(predicted)
    obteing_false_negative(predicted)
    recall=true_positives/(true_positives+false_negatives)
    return recall

        
def obteing_true_positives(predicted):
    global true_positives 
    for value in predicted:
        if value in verdaderos:
            true_positives+=1
            
def obteing_false_negative(predicted):
    global false_negatives
    set_predicted=set(predicted)
    set_verdaderos=set(verdaderos)
    false_negatives_list=list(set_verdaderos-set_predicted)
    false_negatives=len(false_negatives_list)
    
    
            

            

            
    