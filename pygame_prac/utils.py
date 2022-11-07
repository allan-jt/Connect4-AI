from typing import Union

list_tuple = Union[tuple, list]

def center_coordinate(screen_hw:list_tuple, shape_hw:list_tuple) -> list_tuple:
	return (screen_hw[0]/2 - shape_hw[0]/2, screen_hw[1]/2 - shape_hw[1]/2)	
	