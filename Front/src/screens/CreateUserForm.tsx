import { TextField } from "@mui/material";
import axios from "axios";
import { useEffect, useState } from "react";
import LoadingButton from '@mui/lab/LoadingButton';

function CreateUserForm(){

    const [title,setTitle]=useState("");
    const [content,setContent]=useState("");
    const [project,setProject]=useState("");
    const [startDate,setStartDate]=useState("");
    const [endDate,setEndDate]=useState("");
    const [hoursPerDay, setHoursPerDay]=useState("")
    const [saving,setSaving]=useState(false);
    const [posts,setPosts]=useState([]);
    function save(){
        setSaving(true);
        axios.post("http://localhost:8000/post/create",{
            title:title,
            content:content,
            project:project,
            startDate:startDate,
            endDate:endDate,
            hoursPerDay:hoursPerDay,
        }).then((response)=>{
            setSaving(false);
            listPosts();
        })
    }
    function listPosts(){
        axios.get("http://localhost:8000/post/list").then((response)=>{
            setPosts(response.data)
        })
    }
    useEffect(()=>{
        listPosts();
    },[])
    return (
        <div style={{marginTop:30}}>
            <div>
            <TextField id="outlined-basic" label="Title" variant="outlined" value={title} onChange={(event)=>{
                const {value}=event.target
                setTitle(value)
            }} />
            <TextField id="outlined-basic" label="Content" variant="outlined" value={content} onChange={(event)=>{
                const {value}=event.target
                setContent(value)
            }}/>
            <TextField id="outlined-basic" label="Project" variant="outlined" value={project} onChange={(event)=>{
                const {value}=event.target
                setProject(value)
            }} />
            <TextField id="outlined-basic" label="startDate" variant="outlined" value={startDate} onChange={(event)=>{
                const {value}=event.target
                setStartDate(value)
            }} />
            <TextField id="outlined-basic" label="endDate" variant="outlined" value={endDate} onChange={(event)=>{
                const {value}=event.target
                setEndDate(value)
            }} />
            <TextField id="outlined-basic" label="HoursPerDay" variant="outlined" value={hoursPerDay} onChange={(event)=>{
                const {value}=event.target
                setHoursPerDay(value)
            }} />
            <LoadingButton loading={saving} variant="contained" onClick={save}>Save</LoadingButton>
            </div>
            <div>
                {posts.map((post:any)=>{
                    var a = post.status
                    var status = ""
                    if (a==true) {status="Completado"}
                    else {status="No completado"}
                    return <>
                        <p>{post.title} {post.content} {post.project} {post.startDate} {post.endDate} {post.hoursPerDay} {status}</p>
                    </>
                })}
            </div>

        </div>
    );

}

export default CreateUserForm;