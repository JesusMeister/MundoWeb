import React, { useState } from "react";
import Button from '@mui/material/Button';
import { TextField } from "@mui/material";

function Example(){
    const [contador,setContador]=useState(0);
    const [name,setName]=useState("");
    function sumaContador(){
        console.log("Llamando a la funcion sumar")
        setContador(contador+1);
        console.log("Terminando la funcion sumar")
    }
    function restarContador(){
        console.log("Llamando a la funcion sumar")
        setContador(contador-1);
        console.log("Terminando la funcion sumar")
    }

    function onChangeInput(event:any){
        const {value}=event.target
        setName(value)
    }


    return (
        <div>
            {name==="" &&
                <div>
                    <h1>Whats your Name?</h1>

                </div>
            }
            {name!=="" &&
                <div>
                    <h1>Hello {name}, your count is {contador}</h1>
                </div>
            }
            <TextField id="outlined-basic" label="Outlined" variant="outlined" value={name} onChange={onChangeInput}/>

            {name!=="" &&
                <div>
                    <Button variant="contained" onClick={sumaContador}>Sumar</Button>
                    <Button variant="contained" onClick={restarContador}>Restar</Button>        
                </div>


            }
        </div>
    );


}
export default Example;