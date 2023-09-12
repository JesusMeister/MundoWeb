import { Box, Grid, Tab, Tabs } from "@mui/material";
import "./PokemonInfo.css";
import React from "react";
import { Pokemon } from "../../models/Pokemon";
interface TabPanelProps {
    children?: React.ReactNode;
    index: number;
    value: number;
}

function CustomTabPanel(props: TabPanelProps) {
    const { children, value, index, ...other } = props;

    return (
        <div
            role="tabpanel"
            hidden={value !== index}
            id={`simple-tabpanel-${index}`}
            aria-labelledby={`simple-tab-${index}`}
            {...other}
        >
            {value === index && (
                <Box sx={{ p: 3 }}>
                    <div>{children}</div>
                </Box>
            )}
        </div>
    );
}

interface PokemonInfoProps {
    pokemon: Pokemon
}

function PokemonInfo(props: PokemonInfoProps) {
    const [value, setValue] = React.useState(0);
    const handleChange = (event: React.SyntheticEvent, newValue: number) => {
        setValue(newValue);
    };
    // borderBottom: 1, borderColor: 'divider'
    return (
        <div className="TVFrame">
            <div className="TV">
                <Grid container>
                    <Grid item xs={6}>
                        <h1 className="Name">{props.pokemon.name}</h1>
                        <img className="Image" src={props.pokemon.sprites.other["official-artwork"].front_default} alt={props.pokemon.name + " image"}></img>
                    </Grid>
                    <Grid container xs={6}>
                        <Grid item xs={12}>
                            <Tabs value={value} onChange={handleChange} aria-label="basic tabs example">
                                <Tab style={{ color: "white" }} label="Moves" />
                                <Tab style={{ color: "white" }} label="Abilities" />
                            </Tabs>
                        </Grid>
                        <Grid item xs={12}>
                            <CustomTabPanel value={value} index={0}>
                                <div className="Info">
                                    <ul>
                                        {props.pokemon.moves.map((move, index) => {
                                            return <li key={index}>{move.move.name}</li>
                                        })}
                                    </ul>
                                </div>
                            </CustomTabPanel>
                            <CustomTabPanel value={value} index={1}>
                                <div className="Info">
                                    <ul>
                                        {props.pokemon.abilities.map((ability, index) => {
                                            return <li key={index}>{ability.ability.name}</li>
                                        })}
                                    </ul>
                                </div>
                            </CustomTabPanel>
                        </Grid>
                    </Grid>
                </Grid>
            </div>
        </div>
    )
}

export default PokemonInfo;