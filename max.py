//Procedure that will be called each time when raspberry pi receives data
procedure subscribe(topic,data)
    if topic=='esp'
        espid = data[espid]
        status = data[status]
        new_block = new Block(espid,status)
        insert_into_database(new_block)
        blockchain_publish(new_block)
//procedure ot insert data into database
procedure insert_into_database(block)
    cursor = connect(server,user,password,databasename)
    cursor.query('insert into block values(block.espid,block.status,block.hash)')
//procedure that will publish the data into blockchain nodes
procedure blockchain_publish(nodelist,block)
    for each node in nodelist
        send(node,block)

//procedure which will be called each time a new node is added in database
procedure new_node_add(nodeid)
    file = openfile(blocks)
    file.append(nodeid)
    file.close()
//procedure that wiill keep listening to the new node
procedure listen_to_new_node(new_node_add,new_node)
    new_node_add(new_node)



# These procedures will be called on blockchain nodes
//procedure addblock(block)
    file = openfile(myblocks)
    file.append(block)
    file.close()
