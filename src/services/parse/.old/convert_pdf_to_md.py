from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
import time
from datetime import datetime

WORK_DIR = Path(r"C:\Users\muril\flutter_apps\flutter_app_260303\dev\parse\ssg_docling_pdf_to_md")
PAGES_PER_PART = 10
MAX_PARTS = None  # None = processar todo o PDF
ENABLE_OCR = True  # Teste com captura de imagens


def get_pdf_files(work_dir: Path) -> list[Path]:
    """Retorna lista de PDFs na pasta, excluindo partes já criadas."""
    all_pdfs = list(work_dir.glob("*.pdf"))
    
    original_pdfs = []
    for pdf in all_pdfs:
        name = pdf.stem
        if "_" in name and name.split("_")[-1].isdigit():
            continue
        original_pdfs.append(pdf)
    
    return original_pdfs


def split_pdf(input_path: Path, pages_per_part: int, max_parts: int = None) -> list[Path]:
    """Divide PDF em partes de N páginas."""
    reader = PdfReader(str(input_path))
    total_pages = len(reader.pages)
    base_name = input_path.stem
    output_dir = input_path.parent
    part_files = []

    parts_to_create = max_parts if max_parts else (total_pages + pages_per_part - 1) // pages_per_part

    for start in range(0, parts_to_create * pages_per_part, pages_per_part):
        part_num = start // pages_per_part + 1
        end = min(start + pages_per_part, total_pages)
        
        if start >= total_pages:
            break
        
        writer = PdfWriter()
        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])
        
        part_name = f"{base_name}_{part_num:03d}.pdf"
        part_path = output_dir / part_name
        with open(part_path, "wb") as f:
            writer.write(f)
        part_files.append(part_path)

    return part_files


def convert_pdf_to_md(pdf_path: Path, output_path: Path) -> float:
    """Converte PDF para MD."""
    start_time = time.time()
    
    pipeline_options = PdfPipelineOptions()
    pipeline_options.do_ocr = ENABLE_OCR
    pipeline_options.do_table_structure = True
    pipeline_options.table_structure_options.mode = TableFormerMode.FAST
    
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
        }
    )
    
    result = converter.convert(str(pdf_path))
    md_content = result.document.export_to_markdown()
    output_path.write_text(md_content, encoding="utf-8")
    
    elapsed = time.time() - start_time
    return elapsed


def process_pdf(pdf_path: Path, pages_per_part: int):
    """Processa um PDF: divide, converte e combina."""
    base_name = pdf_path.stem
    output_dir = pdf_path.parent
    
    print(f"\n{'='*60}")
    print(f"Processando: {pdf_path.name}")
    print(f"{'='*60}")
    
    print(f"\nDividindo PDF...")
    part_files = split_pdf(pdf_path, pages_per_part, MAX_PARTS)
    print(f"  -> {len(part_files)} partes criadas")
    
    md_files = []
    
    print(f"\nConvertendo partes...")
    for i, part_file in enumerate(part_files, 1):
        md_file = part_file.with_suffix(".md")
        
        elapsed = convert_pdf_to_md(part_file, md_file)
        md_files.append(md_file)
        
        remaining = len(part_files) - i
        eta = elapsed * remaining / 60
        print(f"  [{i}/{len(part_files)}] {part_file.name} -> {md_file.name} ({elapsed:.1f}s) | ETA: {eta:.1f}min")
    
    print(f"\nCombinando {len(md_files)} arquivos MD...")
    combined_md = output_dir / f"{base_name}.md"
    with open(combined_md, "w", encoding="utf-8") as out:
        for md_file in md_files:
            content = md_file.read_text(encoding="utf-8")
            out.write(content)
            out.write("\n\n---\n\n")
    
    file_size = combined_md.stat().st_size / 1024 / 1024
    print(f"\n✓ Concluido: {combined_md.name} ({file_size:.2f} MB)")
    return combined_md


def main():
    print(f"Pasta de trabalho: {WORK_DIR}")
    print(f"Paginas por parte: {PAGES_PER_PART}")
    print(f"Maximo de partes: {MAX_PARTS}")
    print(f"OCR habilitado: {ENABLE_OCR}")
    print(f"Inicio: {datetime.now().strftime('%H:%M:%S')}")
    print("-" * 60)
    
    pdf_files = get_pdf_files(WORK_DIR)
    
    if not pdf_files:
        print("Nenhum PDF encontrado na pasta!")
        return
    
    print(f"PDFs encontrados: {len(pdf_files)}")
    for pdf in pdf_files:
        print(f"  - {pdf.name}")
    
    total_start = time.time()
    
    for i, pdf_path in enumerate(pdf_files, 1):
        print(f"\n[{i}/{len(pdf_files)}] Processando PDF")
        process_pdf(pdf_path, PAGES_PER_PART)
    
    total_time = time.time() - total_start
    
    print("\n" + "=" * 60)
    print(f"TUDO CONCLUIDO!")
    print(f"Total de tempo: {total_time/60:.1f} minutos")
    print(f"Fim: {datetime.now().strftime('%H:%M:%S')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
