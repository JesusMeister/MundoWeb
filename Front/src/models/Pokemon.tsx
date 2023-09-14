export type Pokemon={
    id:number,
    name:string,
    abilities:AbilityOuter[],
    moves:MoveOuter[],
    sprites:Sprites
}

export type AbilityOuter={
    ability:AbilityInner
}

export type AbilityInner={
    name:string
}

export type MoveOuter={
    move:MoveInner
}

export type MoveInner={
    name:string
}

export type Sprites={
    other:Other
}

export type Other={
    "official-artwork":OfficialArtwork
}

export type OfficialArtwork={
    front_default:string,
}