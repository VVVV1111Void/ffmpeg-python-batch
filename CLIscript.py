# The main script for the file
import innerlib
supported = [
    'mp3', 'mp4', 'opus', 'ogg', 'webm'
]
def ask():
    try:
        print('\n Please type or paste the file directory of the files you are trying to convert.')
        target_dir = str(input("\n Enter the path of your file: "))

        if innerlib.verify_dir(target_dir): # Verifies if the folder exists
            ext = str(input("\n Please enter source file extension, eg. 'mp3'(without .): "))
            tar = str(input("\n Please enter target file extension, eg. 'mp3'(without .): "))

            if innerlib.verify_ext(ext, supported) and innerlib.verify_ext(tar, supported): # verifies if the extension is supported
                innerlib.convert_dir(target_dir, tar, ext )
                print('\n Conversion success!')
                return 0

            else:
                raise Exception('\n Unable to verify extensions. / Unsupported extensions')
        else:
            raise Exception('\n Unable to find directory')

    except Exception as e:
        print(e)
        print('\n Would you like to try again? (Y or N)')
        user_input = str(input("")).lower()
        if user_input[0] == 'y':
            ask()
        else:
            return 1

        

if __name__ == "__main__":
    print('\n Hello!')
    print('Press Ctrl C to cancel anytime!')
    ask()
