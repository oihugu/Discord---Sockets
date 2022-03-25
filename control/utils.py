import uuid

def generate_id(id_list):
    temp_id = str(uuid.uuid4())
    
    if temp_id not in id_list:
        id_list.append(temp_id)
        return temp_id
    else:
        return generate_id(id_list)