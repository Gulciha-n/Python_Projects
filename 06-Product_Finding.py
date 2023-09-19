import PyPDF2

def search_number_in_pdf(pdf_path, target_number):
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        num_pages = len(pdf_reader.pages)

        for page_number in range(num_pages):
            page = pdf_reader.pages[page_number]
            page_text = page.extract_text()

            lines = page_text.split('\n')
            for line_number, line in enumerate(lines, start=1):
                if target_number in line:
                    return f"Sayı {target_number}, {page_number+1}. sayfanın {line_number}. satırında bulundu."
    
    return "Sayı bulunamadı."

pdf_path = r"C:\Users\Gulcihan\Desktop\Python\BY MURAT BABY STOK (1).pdf" # PDF dosyasının yolunu belirtin
target_number = input("Aranacak sayıyı girin: ")  # Kullanıcıdan sayıyı alın

result = search_number_in_pdf(pdf_path, target_number)
print(result)
