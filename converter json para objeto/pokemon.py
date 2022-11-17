from typing import List, Optional, Dict, Any


class Species:
    name: str
    url: str

    def __init__(self, name: str, url: str) -> None:
        self.name = name
        self.url = url


class Ability:
    ability: Species
    is_hidden: bool
    slot: int

    def __init__(self, ability: Species, is_hidden: bool, slot: int) -> None:
        self.ability = ability
        self.is_hidden = is_hidden
        self.slot = slot


class GameIndex:
    game_index: int
    version: Species

    def __init__(self, game_index: int, version: Species) -> None:
        self.game_index = game_index
        self.version = version


class VersionGroupDetail:
    level_learned_at: int
    move_learn_method: Species
    version_group: Species

    def __init__(self, level_learned_at: int, move_learn_method: Species, version_group: Species) -> None:
        self.level_learned_at = level_learned_at
        self.move_learn_method = move_learn_method
        self.version_group = version_group


class Move:
    move: Species
    version_group_details: List[VersionGroupDetail]

    def __init__(self, move: Species, version_group_details: List[VersionGroupDetail]) -> None:
        self.move = move
        self.version_group_details = version_group_details


class RedBlue:
    back_default: str
    back_gray: str
    back_transparent: str
    front_default: str
    front_gray: str
    front_transparent: str

    def __init__(self, back_default: str, back_gray: str, back_transparent: str, front_default: str, front_gray: str, front_transparent: str) -> None:
        self.back_default = back_default
        self.back_gray = back_gray
        self.back_transparent = back_transparent
        self.front_default = front_default
        self.front_gray = front_gray
        self.front_transparent = front_transparent


class GenerationI:
    red_blue: RedBlue
    yellow: RedBlue

    def __init__(self, red_blue: RedBlue, yellow: RedBlue) -> None:
        self.red_blue = red_blue
        self.yellow = yellow


class Crystal:
    back_default: str
    back_shiny: str
    back_shiny_transparent: str
    back_transparent: str
    front_default: str
    front_shiny: str
    front_shiny_transparent: str
    front_transparent: str

    def __init__(self, back_default: str, back_shiny: str, back_shiny_transparent: str, back_transparent: str, front_default: str, front_shiny: str, front_shiny_transparent: str, front_transparent: str) -> None:
        self.back_default = back_default
        self.back_shiny = back_shiny
        self.back_shiny_transparent = back_shiny_transparent
        self.back_transparent = back_transparent
        self.front_default = front_default
        self.front_shiny = front_shiny
        self.front_shiny_transparent = front_shiny_transparent
        self.front_transparent = front_transparent


class Gold:
    back_default: str
    back_shiny: str
    front_default: str
    front_shiny: str
    front_transparent: Optional[str]

    def __init__(self, back_default: str, back_shiny: str, front_default: str, front_shiny: str, front_transparent: Optional[str]) -> None:
        self.back_default = back_default
        self.back_shiny = back_shiny
        self.front_default = front_default
        self.front_shiny = front_shiny
        self.front_transparent = front_transparent


class GenerationIi:
    crystal: Crystal
    gold: Gold
    silver: Gold

    def __init__(self, crystal: Crystal, gold: Gold, silver: Gold) -> None:
        self.crystal = crystal
        self.gold = gold
        self.silver = silver


class Emerald:
    front_default: str
    front_shiny: str

    def __init__(self, front_default: str, front_shiny: str) -> None:
        self.front_default = front_default
        self.front_shiny = front_shiny


class GenerationIii:
    emerald: Emerald
    firered_leafgreen: Gold
    ruby_sapphire: Gold

    def __init__(self, emerald: Emerald, firered_leafgreen: Gold, ruby_sapphire: Gold) -> None:
        self.emerald = emerald
        self.firered_leafgreen = firered_leafgreen
        self.ruby_sapphire = ruby_sapphire


class Home:
    front_default: str
    front_female: None
    front_shiny: str
    front_shiny_female: None

    def __init__(self, front_default: str, front_female: None, front_shiny: str, front_shiny_female: None) -> None:
        self.front_default = front_default
        self.front_female = front_female
        self.front_shiny = front_shiny
        self.front_shiny_female = front_shiny_female


class DreamWorld:
    front_default: str
    front_female: None

    def __init__(self, front_default: str, front_female: None) -> None:
        self.front_default = front_default
        self.front_female = front_female


class GenerationVii:
    icons: DreamWorld
    ultra_sun_ultra_moon: Home

    def __init__(self, icons: DreamWorld, ultra_sun_ultra_moon: Home) -> None:
        self.icons = icons
        self.ultra_sun_ultra_moon = ultra_sun_ultra_moon


class GenerationViii:
    icons: DreamWorld

    def __init__(self, icons: DreamWorld) -> None:
        self.icons = icons


class OfficialArtwork:
    front_default: str

    def __init__(self, front_default: str) -> None:
        self.front_default = front_default


class Other:
    dream_world: DreamWorld
    home: Home
    official_artwork: OfficialArtwork

    def __init__(self, dream_world: DreamWorld, home: Home, official_artwork: OfficialArtwork) -> None:
        self.dream_world = dream_world
        self.home = home
        self.official_artwork = official_artwork


class GenerationV:
    black_white: 'Sprites'

    def __init__(self, black_white: 'Sprites') -> None:
        self.black_white = black_white


class GenerationIv:
    diamond_pearl: 'Sprites'
    heartgold_soulsilver: 'Sprites'
    platinum: 'Sprites'

    def __init__(self, diamond_pearl: 'Sprites', heartgold_soulsilver: 'Sprites', platinum: 'Sprites') -> None:
        self.diamond_pearl = diamond_pearl
        self.heartgold_soulsilver = heartgold_soulsilver
        self.platinum = platinum


class Versions:
    generation_i: GenerationI
    generation_ii: GenerationIi
    generation_iii: GenerationIii
    generation_iv: GenerationIv
    generation_v: GenerationV
    generation_vi: Dict[str, Home]
    generation_vii: GenerationVii
    generation_viii: GenerationViii

    def __init__(self, generation_i: GenerationI, generation_ii: GenerationIi, generation_iii: GenerationIii, generation_iv: GenerationIv, generation_v: GenerationV, generation_vi: Dict[str, Home], generation_vii: GenerationVii, generation_viii: GenerationViii) -> None:
        self.generation_i = generation_i
        self.generation_ii = generation_ii
        self.generation_iii = generation_iii
        self.generation_iv = generation_iv
        self.generation_v = generation_v
        self.generation_vi = generation_vi
        self.generation_vii = generation_vii
        self.generation_viii = generation_viii


class Sprites:
    back_default: str
    back_female: None
    back_shiny: str
    back_shiny_female: None
    front_default: str
    front_female: None
    front_shiny: str
    front_shiny_female: None
    other: Optional[Other]
    versions: Optional[Versions]
    animated: Optional['Sprites']

    def __init__(self, back_default: str, back_female: None, back_shiny: str, back_shiny_female: None, front_default: str, front_female: None, front_shiny: str, front_shiny_female: None, other: Optional[Other], versions: Optional[Versions], animated: Optional['Sprites']) -> None:
        self.back_default = back_default
        self.back_female = back_female
        self.back_shiny = back_shiny
        self.back_shiny_female = back_shiny_female
        self.front_default = front_default
        self.front_female = front_female
        self.front_shiny = front_shiny
        self.front_shiny_female = front_shiny_female
        self.other = other
        self.versions = versions
        self.animated = animated


class Stat:
    base_stat: int
    effort: int
    stat: Species

    def __init__(self, base_stat: int, effort: int, stat: Species) -> None:
        self.base_stat = base_stat
        self.effort = effort
        self.stat = stat


class TypeElement:
    slot: int
    type: Species

    def __init__(self, slot: int, type: Species) -> None:
        self.slot = slot
        self.type = type


class Pokemon:
    abilities: List[Ability]
    base_experience: int
    forms: List[Species]
    game_indices: List[GameIndex]
    height: int
    held_items: List[Any]
    id: int
    is_default: bool
    location_area_encounters: str
    moves: List[Move]
    name: str
    order: int
    past_types: List[Any]
    species: Species
    sprites: Sprites
    stats: List[Stat]
    types: List[TypeElement]
    weight: int

    def __init__(self, abilities: List[Ability], base_experience: int, forms: List[Species], game_indices: List[GameIndex], height: int, held_items: List[Any], id: int, is_default: bool, location_area_encounters: str, moves: List[Move], name: str, order: int, past_types: List[Any], species: Species, sprites: Sprites, stats: List[Stat], types: List[TypeElement], weight: int) -> None:
        self.abilities = abilities
        self.base_experience = base_experience
        self.forms = forms
        self.game_indices = game_indices
        self.height = height
        self.held_items = held_items
        self.id = id
        self.is_default = is_default
        self.location_area_encounters = location_area_encounters
        self.moves = moves
        self.name = name
        self.order = order
        self.past_types = past_types
        self.species = species
        self.sprites = sprites
        self.stats = stats
        self.types = types
        self.weight = weight
