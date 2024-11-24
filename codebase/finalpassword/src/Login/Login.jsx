import { useState } from "react";
import Button from "../Button/Button";
import Input from "../Input/Input";
export default function Login(){
    const [option, selectedOption] = useState('');
    let logIn = false;

return(
    <div>
        <Button onClick = {logIn = true}>Sign In</Button>
        <Button onClick = {logIn = false}>Sign Up</Button>
        <Input label="username: " type="text"></Input>
        <Input label="email: " type="text"></Input>
        <Button>{logIn ? "Sign In" : "Sign Up"}</Button>
    </div>
);
}