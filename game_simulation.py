
import updateGame as upG
import get_field_and_save_field as gf_sf
import property


# getField
host = gf_sf.get_field_for_user(property.name_host, property.game_id)
join = gf_sf.get_field_for_user(property.name_join, property.game_id)

# ship_places
host_ship_place = gf_sf.ships_place(host)
join_ship_place = gf_sf.ships_place(join)

# saveField
gf_sf.save_field(host_ship_place)
gf_sf.save_field(join_ship_place)

# обновление состояния игры
upG.get_game_info()
upG.get_boards('hostField', upG.game_reques(upG.game_id))
upG.get_boards('joinField', upG.game_reques(upG.game_id))