import "./Button.css"
import Button from '@mui/material/Button';

interface ButtonProps{
    title:string;
    onPress:()=>void;
}

function ButtonCustom(props:ButtonProps){
    return (
        <Button variant="contained">Contained</Button>
    )
}

export default Button;