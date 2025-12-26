import express from 'express'
import dotenv from 'dotenv/config'

import {v4 as uuidv4} from 'uuid'
import { users, messages } from './users.js'

const PORT = process.env.PORT || 3030;

const app = express();


app.use(express.json());
app.use(express.urlencoded({extended: true}));


app.use((req, res, next)=>{
    req.me = users[1];
    next();
})


app.get('/users', (req, res)=>{
    return res.send(Object.values(users));
});

app.get('/users/:userId', (req, res)=>{
    return res.send(users[req.params.userId]);
})
app.post('/users', (req, res)=>{
    return res.send("POST HTTP method on /users");
});

app.put('/users/:userId', (req, res)=>{
    return res.send(`PUT HTTP method on users/${req.params.userId} resource`);
});

app.delete('/users/:userId', (req, res)=>{
    return res.send(`DELETE HTTP method on users/${req.params.userId} resource`);
});

app.get('/messages', (req, res)=>{
    return res.send(Object.values(messages));
})

app.get('/messages/:messageId', (req, res)=>{
    return res.send(messages[req.params.messageId]);
})

app.post('/messages', (req, res)=>{
    const id = uuidv4();
    const message = {
        id: id,
        text: req.body.text,
        userId: req.me.id,
    }

    messages[id] = message
    return res.send(message)
})

app.listen(PORT, ()=>{
    console.log(`server running on ${PORT}`)
});