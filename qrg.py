# imports
import sys
import qrcode
import qrcode.constants

# generation function
def generate_qr_code(data, output_file):
    if not isinstance(data, str) or not data.strip():
        raise ValueError("Invalid data string.")
    if not isinstance(output_file, str) or not output_file.strip():
        raise ValueError("Invalid output file path.")
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data.strip())
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file.strip())

# main
def main():
    if len(sys.argv) < 3:
        print("Usage: python qr_generator.py <string_to_encode> <output_file.png>")
        sys.exit(1)
    data = sys.argv[1]
    output_file = sys.argv[2]
    generate_qr_code(data, output_file)

# execution
if __name__ == "__main__":
    main()
