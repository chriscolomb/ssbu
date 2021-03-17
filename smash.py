## Importing Necessary Modules
import requests  # to get image from the web
import shutil  # to save it locally

def download_image(image_url, file_name):
    # Open the url image, set stream to True, this will return the stream content.
    r = requests.get(image_url, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(file_name, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

        print('Image sucessfully downloaded: ', file_name)
    else:
        print('Image couldn\'t be retreived.')


fighters = ['mario', 'donkey_kong', 'link', 'samus', 'dark_samus', 'yoshi', 'kirby', 'fox', 'pikachu', 'luigi', 'ness',
            'captain_falcon', 'jigglypuff', 'peach', 'daisy', 'bowser', 'ice_climbers', 'sheik', 'zelda', 'dr_mario',
            'pichu', 'falco', 'marth', 'lucina', 'young_link', 'ganondorf', 'mewtwo', 'roy', 'chrom',
            'mr_game_and_watch', 'meta_knight', 'pit', 'dark_pit', 'zero_suit_samus', 'wario', 'snake', 'ike',
            'pokemon_trainer', 'diddy_kong', 'lucas', 'sonic', 'king_dedede', 'olimar', 'lucario', 'rob', 'toon_link',
            'wolf', 'villager', 'mega_man', 'wii_fit_trainer', 'rosalina_and_luma', 'little_mac', 'greninja',
            'mii_fighter', 'palutena', 'pac_man', 'robin', 'shulk', 'bowser_jr', 'duck_hunt', 'ryu', 'ken', 'cloud',
            'corrin', 'bayonetta', 'inkling', 'ridley', 'simon', 'richter', 'king_k_rool', 'isabelle', 'incineroar',
            'piranha_plant', 'joker', 'hero', 'banjo_and_kazooie', 'terry', 'byleth', 'minmin', 'steve', 'sephiroth',
            'pyra']

alts = ['main', 'main2', 'main3', 'main4', 'main5', 'main6', 'main7', 'main8']


def main():
    url = "https://www.smashbros.com/assets_v2/img/fighter/"
    for fighter in fighters:
        if fighter != 'mii_fighter':
            for alt in alts:
                image_url = url + fighter + '/' + alt + '.png'
                file_name = str("{:02d}".format(fighters.index(fighter) + 1)) + '_' + fighter + '_' + alt + '.png'
                download_image(image_url, file_name)
        elif fighter == 'mii_fighter':
            image_url = url + fighter + '/' + alts[0] + '.png'
            file_name = str("{:02d}".format(fighters.index(fighter) + 1)) + '_' + fighter + '_' + alts[0] + '.png'
            download_image(image_url, file_name)


if __name__ == "__main__":
    main()
