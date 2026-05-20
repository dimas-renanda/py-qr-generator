#!/usr/bin/env python3
"""Generate QR codes from CLI."""
import sys, argparse

def main():
    parser = argparse.ArgumentParser(description="QR Code Generator")
    parser.add_argument("text", help="Text or URL to encode")
    parser.add_argument("--output", "-o", default="qr.png", help="Output file (default: qr.png)")
    parser.add_argument("--size", "-s", type=int, default=10, help="Box size in pixels")
    args = parser.parse_args()

    try:
        import qrcode
    except ImportError:
        print("Install qrcode: pip install qrcode[pil]"); sys.exit(1)

    qr = qrcode.QRCode(box_size=args.size, border=4,
                       error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(args.text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(args.output)
    print(f"✅ QR code saved to {args.output}")
    print(f"   Content: {args.text}")

    # Also print ASCII version
    qr2 = qrcode.QRCode(border=1)
    qr2.add_data(args.text)
    qr2.make(fit=True)
    qr2.print_ascii(invert=True)

main()
