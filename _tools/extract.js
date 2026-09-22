const fs = require('fs');
const { PDFParse } = require('pdf-parse');
(async () => {
  const parser = new PDFParse({ data: new Uint8Array(fs.readFileSync('../Vinodh CV.PDF.pdf')) });
  const result = await parser.getText();
  console.log('PAGES:', result.pages?.length ?? result.total ?? '?');
  console.log(JSON.stringify(Object.keys(result)));
  for (const p of (result.pages || [])) {
    console.log(`--- PAGE ${p.pageNumber ?? p.num ?? ''} ---`);
    console.log(p.text);
  }
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
