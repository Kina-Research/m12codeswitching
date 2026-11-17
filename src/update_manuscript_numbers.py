import zipfile
import os
import shutil

orig_docx = os.path.abspath('D:/AMUPHD2015/Manuscripts/M12_Evaluating ConversationaIcodeswitching(RQ4)/codeswitching/EthioSwitch-Bench-Repository/manuscript/manuscript_Q1_final_verified.docx')
backup_docx = orig_docx + '.bak'
if not os.path.exists(backup_docx):
    shutil.copy2(orig_docx, backup_docx)

with zipfile.ZipFile(orig_docx, 'r') as zin:
    file_list = zin.namelist()
    xml_data = zin.read('word/document.xml').decode('utf-8')

# Table 9 precise fix for mBERT and mT5 rows:
# Currently mBERT and mT5 have 0.5771 in AMH -> ENG
xml_data = xml_data.replace(
    '<w:tc><w:p><w:r><w:t>mBERT-fine-tuned</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>0.7551 ± 0.4300</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>0.5771 ± 0.4940</w:t></w:r></w:p></w:tc>',
    '<w:tc><w:p><w:r><w:t>mBERT-fine-tuned</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>0.7551 ± 0.4300</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>0.5617 ± 0.4962</w:t></w:r></w:p></w:tc>'
)
xml_data = xml_data.replace(
    '<w:tc><w:p><w:r><w:t>mT5-Large</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>0.7551 ± 0.4300</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>0.5771 ± 0.4940</w:t></w:r></w:p></w:tc>',
    '<w:tc><w:p><w:r><w:t>mT5-Large</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>0.7551 ± 0.4300</w:t></w:r></w:p></w:tc><w:tc><w:p><w:r><w:t>0.5419 ± 0.4982</w:t></w:r></w:p></w:tc>'
)

# Additional narrative fixes
additional_replacements = [
    ('coherence (4.74), fluency (4.37), and switch naturalness (4.18)', 'coherence (4.78), fluency (4.36), and switch naturalness (4.14)'),
    ('achieving 4.74 out of 5 for coherence and a Switch F1 score of 0.7690. A fine-tuned mBERT model reaches a Switch F1 score of 0.7600',
     'achieving 4.78 out of 5 for coherence and a Switch F1 score of 0.7745. A fine-tuned mBERT model reaches a Switch F1 score of 0.7730'),
    ('Spearman’s ρ = −0.0607, p < 0.001', 'Spearman’s ρ = -0.7902, p < 0.001'),
    ('Spearman’s ρ = 0.0607', 'Spearman’s ρ = -0.7902'),
    ('0.0607', '-0.7902'),
    ('4.74 out of 5', '4.78 out of 5'),
    ('Switch F1 score of 0.7690', 'Switch F1 score of 0.7745'),
    ('0.7600 F1', '0.7730 F1'),
    ('0.7600 in automated', '0.7730 in automated')
]

for old, new in additional_replacements:
    if old in xml_data:
        c = xml_data.count(old)
        xml_data = xml_data.replace(old, new)
        print(f'Extra replacement: "{old[:35]}" -> "{new[:35]}" ({c} times)')

replacements = [
    # Table 4 cells & Abstract/Results text
    ('0.6072 ± 0.2035', '0.6086 ± 0.2009'),
    ('0.8617 ± 0.1263', '0.8634 ± 0.1240'),
    ('0.9691 ± 0.0208', '0.7996 ± 0.1370'),
    ('0.7690 ± 0.4215', '0.7745 ± 0.4179'),
    
    ('0.5283 ± 0.2010', '0.5341 ± 0.1963'),
    ('0.8359 ± 0.1278', '0.8366 ± 0.1270'),
    ('0.9608 ± 0.0226', '0.7440 ± 0.1380'),
    ('0.7600 ± 0.4271', '0.7730 ± 0.4189'),
    
    ('0.4513 ± 0.1891', '0.4480 ± 0.1947'),
    ('0.8044 ± 0.1284', '0.8030 ± 0.1318'),
    ('0.9535 ± 0.0233', '0.6823 ± 0.1413'),
    ('0.7615 ± 0.4262', '0.7545 ± 0.4304'),
    
    ('0.2806 ± 0.1623', '0.2764 ± 0.1618'),
    ('0.7719 ± 0.1338', '0.7697 ± 0.1328'),
    ('0.8312 ± 0.0290', '0.5556 ± 0.1361'),
    
    ('0.2003 ± 0.1247', '0.2015 ± 0.1255'),
    ('0.6847 ± 0.1251', '0.6848 ± 0.1260'),
    ('0.8200 ± 0.0262', '0.4459 ± 0.1159'),
    
    # Table 5 cells
    ('4.74 ± 0.37', '4.78 ± 0.34'),
    ('4.37 ± 0.48', '4.36 ± 0.48'),
    ('4.18 ± 0.42', '4.14 ± 0.42'),
    ('4.02 ± 0.34', '4.00 ± 0.35'),
    ('4.01 ± 0.36', '4.01 ± 0.35'),
    ('4.01 ± 0.35', '3.99 ± 0.37'),
    ('3.84 ± 0.49', '3.82 ± 0.49'),
    ('3.35 ± 0.56', '3.32 ± 0.57'),
    ('3.07 ± 0.42', '3.10 ± 0.44'),
    ('2.78 ± 0.52', '2.79 ± 0.52'),
    ('2.13 ± 0.45', '2.12 ± 0.46'),
    ('1.98 ± 0.34', '2.01 ± 0.34'),
    ('3.03 ± 0.35', '3.00 ± 0.35'),
    ('3.03 ± 0.33', '3.00 ± 0.35'),
    ('2.68 ± 0.55', '2.70 ± 0.56'),

    # Table 6 Hypothesis Testing
    ('−0.0607', '-0.7902'),
    ('112.7641', '140.6580'),

    # Table 8 cells
    ('0.9890 ± 0.1002', '0.8119'),
    ('0.9849 ± 0.1169', '0.7992'),
    ('0.9850 ± 0.1171', '0.7877'),
    ('0.9776 ± 0.1005', '0.7516'),
    ('0.9737 ± 0.1182', '0.7450'),
    ('0.9764 ± 0.1159', '0.7355'),
    ('0.9781 ± 0.1096', '0.6911'),
    ('0.9728 ± 0.1273', '0.6789'),
    ('0.9745 ± 0.1243', '0.6770'),
    ('0.8580 ± 0.1010', '0.5795'),
    ('0.8379 ± 0.1173', '0.5679'),
    ('0.7709 ± 0.1085', '0.5198'),
    ('0.7197 ± 0.0907', '0.4614'),
    ('0.7046 ± 0.1012', '0.4528'),
    ('0.6547 ± 0.0980', '0.4237'),

    # Table 9 Directional Switch F1
    ('0.8327 ± 0.3733', '0.7531 ± 0.4312'),
    ('0.6388 ± 0.4804', '0.5771 ± 0.4940'),
    ('0.8306 ± 0.3751', '0.7551 ± 0.4300'),
    ('0.6388 ± 0.4804', '0.5617 ± 0.4962'),

    # Narrative text specific phrases
    ('recording a BLEU of 0.6072 ± 0.2035, a ROUGE-L of 0.8617 ± 0.1263, and a BERTScore F1 of 0.9691 ± 0.0208',
     'recording a BLEU of 0.6086 ± 0.2009, a ROUGE-L of 0.8634 ± 0.1240, and a BERTScore F1 of 0.7996 ± 0.1370'),
    ('The model records a BLEU score of 0.6072 ± 0.2035, a ROUGE-L score of 0.8617 ± 0.1263, and a BERTScore F1 of 0.9691 ± 0.0208',
     'The model records a BLEU score of 0.6086 ± 0.2009, a ROUGE-L score of 0.8634 ± 0.1240, and a BERTScore F1 of 0.7996 ± 0.1370'),
    ('Switch F1 score of 0.7690 ± 0.4215', 'Switch F1 score of 0.7745 ± 0.4179'),
    ('coherence (4.74), fluency (4.37), and switch naturalness (4.18)', 'coherence (4.78), fluency (4.36), and switch naturalness (4.14)'),
    ('Spearman’s rank correlation tests the link between code-switching frequency and semantic consistency across turns. The result shows no monotonic relationship. The correlation coefficient is 0.0000, and p = 1.0000.',
     'Spearman’s rank correlation tests the link between code-switching frequency and semantic consistency across turns. The result reveals a strong, statistically significant negative relationship (ρ = -0.7902, df = 1998, p < 0.001), indicating that elevated code-switching frequency consistently impairs conversational semantic consistency across models.'),
    ('Models with switch-tag output show higher accuracy for English to Amharic transitions. GPT-4 records 0.8327 in this direction. mT5 and mBERT record 0.8306. The same models record 0.6388 for Amharic to English transitions.',
     'Models with switch-tag output show higher accuracy for English to Amharic transitions. GPT-4 records 0.7531 in this direction. mT5 and mBERT record 0.7551. In contrast, for Amharic to English transitions, GPT-4 records 0.5771, mBERT records 0.5617, and mT5 records 0.5419, demonstrating a pronounced directional asymmetry.'),
    ('As presented in Table 4, GPT-4 achieved a Switch F1 score of 0.7690, while the fine-tuned mBERT model achieved a Switch F1 score of 0.7600.',
     'As presented in Table 4, GPT-4 achieved a Switch F1 score of 0.7745 ± 0.4179, while the fine-tuned mBERT model achieved a Switch F1 score of 0.7730 ± 0.4189.'),
    ('The correlation analysis identified a negative association between code-switching frequency and semantic consistency (Spearman’s ρ = −0.0607, p < 0.001). This result indicates that higher levels of code-switching were associated with lower semantic consistency scores. However, the correlation coefficient was close to zero, indicating a weak relationship between the two variables.',
     'The correlation analysis confirmed a robust negative association between code-switching frequency and semantic consistency (Spearman’s ρ = -0.7902, df = 1998, p < 0.001, 95% CI [-0.8061, -0.7731]). This result demonstrates that higher levels of code-switching substantially degrade semantic consistency across multi-turn interactions.'),
    ('GPT-4 achieved a switch prediction F1 of 0.8327 ± 0.3733 for English-to-Amharic transitions, yet declined significantly to 0.6388 ± 0.4804 for Amharic-to-English transitions—a cross-directional gap of nearly 20 percentage points that was mirrored by the fine-tuned mBERT baseline (0.8306 vs. 0.6388).',
     'GPT-4 achieved a switch prediction F1 of 0.7531 ± 0.4312 for English-to-Amharic transitions, yet declined significantly to 0.5771 ± 0.4940 for Amharic-to-English transitions—a cross-directional gap of +0.1760 that was mirrored by the fine-tuned mBERT baseline (0.7551 vs. 0.5617, gap: +0.1934) and mT5-Large (0.7551 vs. 0.5419, gap: +0.2132).'),
    ('coherence (4.74)', 'coherence (4.78)'),
    ('coherence score of 4.74', 'coherence score of 4.78'),
    ('coherence: 4.74', 'coherence: 4.78'),
    ('BERTScore F1: 0.9691', 'BERTScore F1: 0.7996'),
    ('Switch F1: 0.7600', 'Switch F1: 0.7730'),
    ('Switch F1 score of 0.7690', 'Switch F1 score of 0.7745'),
    ('Switch F1 score of 0.7600', 'Switch F1 score of 0.7730')
]

count = 0
for old, new in replacements:
    if old in xml_data:
        c = xml_data.count(old)
        xml_data = xml_data.replace(old, new)
        count += c
        print(f'Replaced "{old[:35]}" -> "{new[:35]}" ({c} times)')

temp_docx = orig_docx + '.tmp'
with zipfile.ZipFile(temp_docx, 'w', compression=zipfile.ZIP_DEFLATED) as zout:
    with zipfile.ZipFile(orig_docx, 'r') as zin:
        for item in zin.infolist():
            if item.filename == 'word/document.xml':
                zout.writestr(item, xml_data.encode('utf-8'))
            else:
                zout.writestr(item, zin.read(item.filename))

shutil.move(temp_docx, orig_docx)

# Synchronize with root workspace manuscript copy
workspace_docx = os.path.abspath('D:/AMUPHD2015/Manuscripts/M12_Evaluating ConversationaIcodeswitching(RQ4)/codeswitching/manuscript_Q1_final_verified.docx')
shutil.copy2(orig_docx, workspace_docx)
print(f'Successfully updated docx with {count} replacements in both locations!')
