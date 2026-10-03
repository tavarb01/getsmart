# Picture Plane Faces: prompts para o Gemini

Tudo o que você precisa para gerar as 343 imagens no Gemini, em ordem de uso.

**Como usar**
1. Abra uma conversa nova no Gemini e cole a **mensagem inicial** (seção 1).
2. Mande o **lote de teste** (seção 2) para checar se ele entendeu o modelo.
3. Depois mande os **49 lotes** (seção 4), um por vez. Em cada lote, o Gemini gera uma imagem por resposta e espera você dizer "próxima".
4. Se ele sair do formato (grade, texto na imagem, personagem diferente), cole a **mensagem de correção** (seção 3).

Cada lote é um dos 49 triângulos pequenos: os IDs `XY1` a `XY7` são os 7 pontos dentro do triângulo `XY`.

---

## 1. Mensagem inicial (cole uma vez)

```
Você vai gerar uma série de 343 retratos para um aplicativo de estudo chamado "Picture Plane Faces". Leia tudo antes de começar e responda só "Entendi, pode mandar o primeiro lote."

=== O MODELO: O "GRANDE TRIÂNGULO" DE SCOTT McCLOUD ===
No livro "Understanding Comics" (1993), Scott McCloud organiza todo o vocabulário visual dos quadrinhos num triângulo com três vértices:

1. REALIDADE (canto inferior esquerdo): semelhança com o mundo real. Fotografia, desenho realista, sombreamento, anatomia, textura de pele e cabelo.
2. LINGUAGEM / SIGNIFICADO (canto inferior direito): abstração icônica. O desenho perde detalhes mas mantém o sentido: rosto simplificado, depois um smiley, e no extremo a própria palavra "rosto". Quanto mais simples, mais universal o rosto.
3. PLANO DA IMAGEM (topo): abstração não icônica. Linhas, formas e cores deixam de representar um rosto e passam a valer por si mesmas: cubismo, formas geométricas, campos de cor.

Todo ponto dentro do triângulo é uma mistura desses três polos. Os três pesos sempre somam 100%.

=== POR QUE AS COORDENADAS IMPORTAM ===
Dividi o triângulo em 343 posições (7 × 7 × 7). Cada imagem corresponde a UMA posição exata, identificada por:
- um ID de três dígitos, cada um de 1 a 7 (de 111 a 777). Os dois primeiros dígitos indicam qual dos 49 triângulos menores; o terceiro, qual dos 7 pontos dentro dele.
- três pesos: Realidade (R), Linguagem (L) e Plano da Imagem (P), em porcentagem.

As coordenadas são o ponto central do projeto:
- O estilo de cada imagem deve refletir os pesos com precisão. Uma imagem com R 80% tem que parecer claramente mais realista que uma com R 50%.
- Vizinhos no triângulo devem mudar de estilo aos poucos, sem saltos bruscos. Quando as 343 imagens forem colocadas lado a lado no triângulo, devem formar um mapa contínuo.
- O ID é a chave usada para encaixar cada imagem de volta no aplicativo. Se um ID se perder ou for trocado, a imagem cai no lugar errado.

=== O PERSONAGEM (o mesmo em todas as imagens) ===
Use SEMPRE o mesmo personagem original, para que a única coisa que mude seja o estilo:
- homem jovem, rosto oval, cabelo escuro curto com franja leve, sobrancelhas marcadas, expressão neutra com um leve sorriso;
- camiseta cinza simples de gola redonda;
- não pode lembrar nenhum personagem existente, celebridade ou pessoa real.
No canto da Linguagem ele vira quase um smiley; no topo vira formas abstratas. Ainda assim, é sempre "ele" em outro estilo.

=== ENQUADRAMENTO E FORMATO (igual para todas) ===
- Busto: cabeça e ombros, de frente, centralizado, com a cabeça ocupando cerca de 60% da altura.
- Fundo branco liso.
- Proporção vertical 4:5, em 1080 × 1350 pixels. Esse tamanho preenche a largura da tela do iPhone sem cortar nada.
- UMA imagem por resposta. Nada de grade, colagem, molduras, bordas ou painéis.

=== PROIBIDO DENTRO DA IMAGEM ===
Nenhum texto, letra, número, legenda, assinatura ou marca d'água desenhados na imagem. O ID NÃO deve aparecer na figura. Ele vai somente no texto da sua resposta.

=== COMO TRADUZIR OS PESOS EM ESTILO ===
- R alto: proporções reais, sombreamento com hachura ou pintura, olhos com íris e pálpebras, linhas de expressão. Acima de 85%, acabamento quase fotográfico.
- L alto: poucas linhas, contorno grosso e uniforme, olhos grandes ou em pontos, boca de um traço. Acima de 85%, praticamente um smiley: um círculo, dois pontos e um traço.
- P alto: traços tortos e expressivos; com P médio, feições deslocadas e cubismo; com P alto, formas geométricas e cores chapadas fortes. Acima de 85%, o rosto quase desaparece numa composição abstrata em que só se intui uma cabeça.
- Pesos misturados: combine na proporção. Exemplo: R 40%, L 40%, P 20% = cartum clássico com algum volume e um traço levemente solto. No centro (33/33/33) a imagem não deve parecer nem foto nem ilustração realista: é uma mistura estranha dos três.

=== NOME DO ARQUIVO (obrigatório) ===
Cada imagem deve ter este nome:
  ppf_<ID>_R<r>_L<l>_P<p>.png
Exemplo: ppf_452_R33_L41_P26.png
Escreva o nome exato numa linha logo ACIMA da imagem, no texto da resposta (nunca dentro da imagem):
  Arquivo: ppf_452_R33_L41_P26.png

=== RITMO ===
Eu mando lotes de até 7 posições. Gere UMA imagem por resposta, na ordem do lote, com a linha "Arquivo:" acima. Depois espere eu dizer "próxima". Quando o lote acabar, espere o próximo lote.
```

---

## 2. Lote de teste: pontos extremos

Os 3 cantos, o meio de cada lado e o centro. Se as 7 imagens saírem claramente diferentes, o Gemini entendeu o modelo.

```

Lote de teste: 7 posições bem distantes entre si. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

752 — R 95%, L 2%, P 2%  (canto da Realidade: quase fotográfico)   →  Arquivo: ppf_752_R95_L2_P2.png
773 — R 2%, L 95%, P 2%  (canto da Linguagem: praticamente um smiley)   →  Arquivo: ppf_773_R2_L95_P2.png
114 — R 2%, L 2%, P 95%  (canto do Plano da Imagem: formas abstratas, o rosto quase some)   →  Arquivo: ppf_114_R2_L2_P95.png
765 — R 49%, L 49%, P 2%  (meio da base: cartum clássico com volume)   →  Arquivo: ppf_765_R49_L49_P2.png
267 — R 49%, L 2%, P 49%  (meio do lado esquerdo: realismo expressionista e distorcido)   →  Arquivo: ppf_267_R49_L2_P49.png
326 — R 2%, L 49%, P 49%  (meio do lado direito: ícone gráfico e geométrico)   →  Arquivo: ppf_326_R2_L49_P49.png
441 — R 33%, L 33%, P 33%  (centro: mistura equilibrada e estranha dos três)   →  Arquivo: ppf_441_R33_L33_P33.png
```

---

## 3. Mensagem de correção (use quando ele sair do formato)

```
Os estilos estão no caminho certo, mas preciso corrigir o formato:

1. Uma imagem POR RESPOSTA, separada. Nada de grade ou colagem.
2. NENHUM texto dentro da imagem. O nome do arquivo vai só no texto da sua resposta, acima da imagem.
3. Sempre o MESMO personagem: homem jovem, cabelo escuro curto com franja leve, camiseta cinza de gola redonda.
4. Formato vertical 4:5, 1080 × 1350.
5. Respeite os pesos: a diferença de estilo entre as imagens é o objetivo principal.

Refaça a última imagem seguindo essas regras e depois espere eu dizer "próxima".
```

---

## 4. Os 49 lotes (todas as 343 posições)

Ordem: de cima (Plano da Imagem) para baixo, da esquerda para a direita, igual à numeração dos IDs.

### Lote 1 de 49: triângulo 11 (IDs 111–117)

```
Lote 1/49: triângulo 11. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

111 — R 5%, L 5%, P 90%   →  Arquivo: ppf_111_R5_L5_P90.png
112 — R 10%, L 2%, P 88%   →  Arquivo: ppf_112_R10_L2_P88.png
113 — R 2%, L 10%, P 88%   →  Arquivo: ppf_113_R2_L10_P88.png
114 — R 2%, L 2%, P 95%   →  Arquivo: ppf_114_R2_L2_P95.png
115 — R 6%, L 6%, P 88%   →  Arquivo: ppf_115_R6_L6_P88.png
116 — R 2%, L 6%, P 92%   →  Arquivo: ppf_116_R2_L6_P92.png
117 — R 6%, L 2%, P 92%   →  Arquivo: ppf_117_R6_L2_P92.png
```

### Lote 2 de 49: triângulo 12 (IDs 121–127)

```
Lote 2/49: triângulo 12. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

121 — R 10%, L 10%, P 81%   →  Arquivo: ppf_121_R10_L10_P81.png
122 — R 5%, L 12%, P 83%   →  Arquivo: ppf_122_R5_L12_P83.png
123 — R 12%, L 5%, P 83%   →  Arquivo: ppf_123_R12_L5_P83.png
124 — R 12%, L 12%, P 76%   →  Arquivo: ppf_124_R12_L12_P76.png
125 — R 8%, L 8%, P 84%   →  Arquivo: ppf_125_R8_L8_P84.png
126 — R 12%, L 8%, P 80%   →  Arquivo: ppf_126_R12_L8_P80.png
127 — R 8%, L 12%, P 80%   →  Arquivo: ppf_127_R8_L12_P80.png
```

### Lote 3 de 49: triângulo 13 (IDs 131–137)

```
Lote 3/49: triângulo 13. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

131 — R 19%, L 5%, P 76%   →  Arquivo: ppf_131_R19_L5_P76.png
132 — R 24%, L 2%, P 74%   →  Arquivo: ppf_132_R24_L2_P74.png
133 — R 17%, L 10%, P 74%   →  Arquivo: ppf_133_R17_L10_P74.png
134 — R 17%, L 2%, P 81%   →  Arquivo: ppf_134_R17_L2_P81.png
135 — R 20%, L 6%, P 73%   →  Arquivo: ppf_135_R20_L6_P73.png
136 — R 16%, L 6%, P 78%   →  Arquivo: ppf_136_R16_L6_P78.png
137 — R 20%, L 2%, P 78%   →  Arquivo: ppf_137_R20_L2_P78.png
```

### Lote 4 de 49: triângulo 14 (IDs 141–147)

```
Lote 4/49: triângulo 14. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

141 — R 5%, L 19%, P 76%   →  Arquivo: ppf_141_R5_L19_P76.png
142 — R 10%, L 17%, P 74%   →  Arquivo: ppf_142_R10_L17_P74.png
143 — R 2%, L 24%, P 74%   →  Arquivo: ppf_143_R2_L24_P74.png
144 — R 2%, L 17%, P 81%   →  Arquivo: ppf_144_R2_L17_P81.png
145 — R 6%, L 20%, P 73%   →  Arquivo: ppf_145_R6_L20_P73.png
146 — R 2%, L 20%, P 78%   →  Arquivo: ppf_146_R2_L20_P78.png
147 — R 6%, L 16%, P 78%   →  Arquivo: ppf_147_R6_L16_P78.png
```

### Lote 5 de 49: triângulo 15 (IDs 151–157)

```
Lote 5/49: triângulo 15. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

151 — R 24%, L 10%, P 67%   →  Arquivo: ppf_151_R24_L10_P67.png
152 — R 19%, L 12%, P 69%   →  Arquivo: ppf_152_R19_L12_P69.png
153 — R 26%, L 5%, P 69%   →  Arquivo: ppf_153_R26_L5_P69.png
154 — R 26%, L 12%, P 62%   →  Arquivo: ppf_154_R26_L12_P62.png
155 — R 22%, L 8%, P 70%   →  Arquivo: ppf_155_R22_L8_P70.png
156 — R 27%, L 8%, P 65%   →  Arquivo: ppf_156_R27_L8_P65.png
157 — R 22%, L 12%, P 65%   →  Arquivo: ppf_157_R22_L12_P65.png
```

### Lote 6 de 49: triângulo 16 (IDs 161–167)

```
Lote 6/49: triângulo 16. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

161 — R 10%, L 24%, P 67%   →  Arquivo: ppf_161_R10_L24_P67.png
162 — R 5%, L 26%, P 69%   →  Arquivo: ppf_162_R5_L26_P69.png
163 — R 12%, L 19%, P 69%   →  Arquivo: ppf_163_R12_L19_P69.png
164 — R 12%, L 26%, P 62%   →  Arquivo: ppf_164_R12_L26_P62.png
165 — R 8%, L 22%, P 70%   →  Arquivo: ppf_165_R8_L22_P70.png
166 — R 12%, L 22%, P 65%   →  Arquivo: ppf_166_R12_L22_P65.png
167 — R 8%, L 27%, P 65%   →  Arquivo: ppf_167_R8_L27_P65.png
```

### Lote 7 de 49: triângulo 17 (IDs 171–177)

```
Lote 7/49: triângulo 17. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

171 — R 33%, L 5%, P 62%   →  Arquivo: ppf_171_R33_L5_P62.png
172 — R 38%, L 2%, P 60%   →  Arquivo: ppf_172_R38_L2_P60.png
173 — R 31%, L 10%, P 60%   →  Arquivo: ppf_173_R31_L10_P60.png
174 — R 31%, L 2%, P 67%   →  Arquivo: ppf_174_R31_L2_P67.png
175 — R 35%, L 6%, P 59%   →  Arquivo: ppf_175_R35_L6_P59.png
176 — R 30%, L 6%, P 63%   →  Arquivo: ppf_176_R30_L6_P63.png
177 — R 35%, L 2%, P 63%   →  Arquivo: ppf_177_R35_L2_P63.png
```

### Lote 8 de 49: triângulo 21 (IDs 211–217)

```
Lote 8/49: triângulo 21. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

211 — R 19%, L 19%, P 62%   →  Arquivo: ppf_211_R19_L19_P62.png
212 — R 24%, L 17%, P 60%   →  Arquivo: ppf_212_R24_L17_P60.png
213 — R 17%, L 24%, P 60%   →  Arquivo: ppf_213_R17_L24_P60.png
214 — R 17%, L 17%, P 67%   →  Arquivo: ppf_214_R17_L17_P67.png
215 — R 20%, L 20%, P 59%   →  Arquivo: ppf_215_R20_L20_P59.png
216 — R 16%, L 20%, P 63%   →  Arquivo: ppf_216_R16_L20_P63.png
217 — R 20%, L 16%, P 63%   →  Arquivo: ppf_217_R20_L16_P63.png
```

### Lote 9 de 49: triângulo 22 (IDs 221–227)

```
Lote 9/49: triângulo 22. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

221 — R 5%, L 33%, P 62%   →  Arquivo: ppf_221_R5_L33_P62.png
222 — R 10%, L 31%, P 60%   →  Arquivo: ppf_222_R10_L31_P60.png
223 — R 2%, L 38%, P 60%   →  Arquivo: ppf_223_R2_L38_P60.png
224 — R 2%, L 31%, P 67%   →  Arquivo: ppf_224_R2_L31_P67.png
225 — R 6%, L 35%, P 59%   →  Arquivo: ppf_225_R6_L35_P59.png
226 — R 2%, L 35%, P 63%   →  Arquivo: ppf_226_R2_L35_P63.png
227 — R 6%, L 30%, P 63%   →  Arquivo: ppf_227_R6_L30_P63.png
```

### Lote 10 de 49: triângulo 23 (IDs 231–237)

```
Lote 10/49: triângulo 23. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

231 — R 38%, L 10%, P 52%   →  Arquivo: ppf_231_R38_L10_P52.png
232 — R 33%, L 12%, P 55%   →  Arquivo: ppf_232_R33_L12_P55.png
233 — R 40%, L 5%, P 55%   →  Arquivo: ppf_233_R40_L5_P55.png
234 — R 40%, L 12%, P 48%   →  Arquivo: ppf_234_R40_L12_P48.png
235 — R 37%, L 8%, P 55%   →  Arquivo: ppf_235_R37_L8_P55.png
236 — R 41%, L 8%, P 51%   →  Arquivo: ppf_236_R41_L8_P51.png
237 — R 37%, L 12%, P 51%   →  Arquivo: ppf_237_R37_L12_P51.png
```

### Lote 11 de 49: triângulo 24 (IDs 241–247)

```
Lote 11/49: triângulo 24. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

241 — R 10%, L 38%, P 52%   →  Arquivo: ppf_241_R10_L38_P52.png
242 — R 5%, L 40%, P 55%   →  Arquivo: ppf_242_R5_L40_P55.png
243 — R 12%, L 33%, P 55%   →  Arquivo: ppf_243_R12_L33_P55.png
244 — R 12%, L 40%, P 48%   →  Arquivo: ppf_244_R12_L40_P48.png
245 — R 8%, L 37%, P 55%   →  Arquivo: ppf_245_R8_L37_P55.png
246 — R 12%, L 37%, P 51%   →  Arquivo: ppf_246_R12_L37_P51.png
247 — R 8%, L 41%, P 51%   →  Arquivo: ppf_247_R8_L41_P51.png
```

### Lote 12 de 49: triângulo 25 (IDs 251–257)

```
Lote 12/49: triângulo 25. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

251 — R 24%, L 24%, P 52%   →  Arquivo: ppf_251_R24_L24_P52.png
252 — R 19%, L 26%, P 55%   →  Arquivo: ppf_252_R19_L26_P55.png
253 — R 26%, L 19%, P 55%   →  Arquivo: ppf_253_R26_L19_P55.png
254 — R 26%, L 26%, P 48%   →  Arquivo: ppf_254_R26_L26_P48.png
255 — R 22%, L 22%, P 55%   →  Arquivo: ppf_255_R22_L22_P55.png
256 — R 27%, L 22%, P 51%   →  Arquivo: ppf_256_R27_L22_P51.png
257 — R 22%, L 27%, P 51%   →  Arquivo: ppf_257_R22_L27_P51.png
```

### Lote 13 de 49: triângulo 26 (IDs 261–267)

```
Lote 13/49: triângulo 26. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

261 — R 48%, L 5%, P 48%   →  Arquivo: ppf_261_R48_L5_P48.png
262 — R 52%, L 2%, P 45%   →  Arquivo: ppf_262_R52_L2_P45.png
263 — R 45%, L 10%, P 45%   →  Arquivo: ppf_263_R45_L10_P45.png
264 — R 45%, L 2%, P 52%   →  Arquivo: ppf_264_R45_L2_P52.png
265 — R 49%, L 6%, P 45%   →  Arquivo: ppf_265_R49_L6_P45.png
266 — R 45%, L 6%, P 49%   →  Arquivo: ppf_266_R45_L6_P49.png
267 — R 49%, L 2%, P 49%   →  Arquivo: ppf_267_R49_L2_P49.png
```

### Lote 14 de 49: triângulo 27 (IDs 271–277)

```
Lote 14/49: triângulo 27. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

271 — R 33%, L 19%, P 48%   →  Arquivo: ppf_271_R33_L19_P48.png
272 — R 38%, L 17%, P 45%   →  Arquivo: ppf_272_R38_L17_P45.png
273 — R 31%, L 24%, P 45%   →  Arquivo: ppf_273_R31_L24_P45.png
274 — R 31%, L 17%, P 52%   →  Arquivo: ppf_274_R31_L17_P52.png
275 — R 35%, L 20%, P 45%   →  Arquivo: ppf_275_R35_L20_P45.png
276 — R 30%, L 20%, P 49%   →  Arquivo: ppf_276_R30_L20_P49.png
277 — R 35%, L 16%, P 49%   →  Arquivo: ppf_277_R35_L16_P49.png
```

### Lote 15 de 49: triângulo 31 (IDs 311–317)

```
Lote 15/49: triângulo 31. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

311 — R 19%, L 33%, P 48%   →  Arquivo: ppf_311_R19_L33_P48.png
312 — R 24%, L 31%, P 45%   →  Arquivo: ppf_312_R24_L31_P45.png
313 — R 17%, L 38%, P 45%   →  Arquivo: ppf_313_R17_L38_P45.png
314 — R 17%, L 31%, P 52%   →  Arquivo: ppf_314_R17_L31_P52.png
315 — R 20%, L 35%, P 45%   →  Arquivo: ppf_315_R20_L35_P45.png
316 — R 16%, L 35%, P 49%   →  Arquivo: ppf_316_R16_L35_P49.png
317 — R 20%, L 30%, P 49%   →  Arquivo: ppf_317_R20_L30_P49.png
```

### Lote 16 de 49: triângulo 32 (IDs 321–327)

```
Lote 16/49: triângulo 32. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

321 — R 5%, L 48%, P 48%   →  Arquivo: ppf_321_R5_L48_P48.png
322 — R 10%, L 45%, P 45%   →  Arquivo: ppf_322_R10_L45_P45.png
323 — R 2%, L 52%, P 45%   →  Arquivo: ppf_323_R2_L52_P45.png
324 — R 2%, L 45%, P 52%   →  Arquivo: ppf_324_R2_L45_P52.png
325 — R 6%, L 49%, P 45%   →  Arquivo: ppf_325_R6_L49_P45.png
326 — R 2%, L 49%, P 49%   →  Arquivo: ppf_326_R2_L49_P49.png
327 — R 6%, L 45%, P 49%   →  Arquivo: ppf_327_R6_L45_P49.png
```

### Lote 17 de 49: triângulo 33 (IDs 331–337)

```
Lote 17/49: triângulo 33. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

331 — R 52%, L 10%, P 38%   →  Arquivo: ppf_331_R52_L10_P38.png
332 — R 48%, L 12%, P 40%   →  Arquivo: ppf_332_R48_L12_P40.png
333 — R 55%, L 5%, P 40%   →  Arquivo: ppf_333_R55_L5_P40.png
334 — R 55%, L 12%, P 33%   →  Arquivo: ppf_334_R55_L12_P33.png
335 — R 51%, L 8%, P 41%   →  Arquivo: ppf_335_R51_L8_P41.png
336 — R 55%, L 8%, P 37%   →  Arquivo: ppf_336_R55_L8_P37.png
337 — R 51%, L 12%, P 37%   →  Arquivo: ppf_337_R51_L12_P37.png
```

### Lote 18 de 49: triângulo 34 (IDs 341–347)

```
Lote 18/49: triângulo 34. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

341 — R 38%, L 24%, P 38%   →  Arquivo: ppf_341_R38_L24_P38.png
342 — R 33%, L 26%, P 40%   →  Arquivo: ppf_342_R33_L26_P40.png
343 — R 40%, L 19%, P 40%   →  Arquivo: ppf_343_R40_L19_P40.png
344 — R 40%, L 26%, P 33%   →  Arquivo: ppf_344_R40_L26_P33.png
345 — R 37%, L 22%, P 41%   →  Arquivo: ppf_345_R37_L22_P41.png
346 — R 41%, L 22%, P 37%   →  Arquivo: ppf_346_R41_L22_P37.png
347 — R 37%, L 27%, P 37%   →  Arquivo: ppf_347_R37_L27_P37.png
```

### Lote 19 de 49: triângulo 35 (IDs 351–357)

```
Lote 19/49: triângulo 35. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

351 — R 24%, L 38%, P 38%   →  Arquivo: ppf_351_R24_L38_P38.png
352 — R 19%, L 40%, P 40%   →  Arquivo: ppf_352_R19_L40_P40.png
353 — R 26%, L 33%, P 40%   →  Arquivo: ppf_353_R26_L33_P40.png
354 — R 26%, L 40%, P 33%   →  Arquivo: ppf_354_R26_L40_P33.png
355 — R 22%, L 37%, P 41%   →  Arquivo: ppf_355_R22_L37_P41.png
356 — R 27%, L 37%, P 37%   →  Arquivo: ppf_356_R27_L37_P37.png
357 — R 22%, L 41%, P 37%   →  Arquivo: ppf_357_R22_L41_P37.png
```

### Lote 20 de 49: triângulo 36 (IDs 361–367)

```
Lote 20/49: triângulo 36. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

361 — R 10%, L 52%, P 38%   →  Arquivo: ppf_361_R10_L52_P38.png
362 — R 5%, L 55%, P 40%   →  Arquivo: ppf_362_R5_L55_P40.png
363 — R 12%, L 48%, P 40%   →  Arquivo: ppf_363_R12_L48_P40.png
364 — R 12%, L 55%, P 33%   →  Arquivo: ppf_364_R12_L55_P33.png
365 — R 8%, L 51%, P 41%   →  Arquivo: ppf_365_R8_L51_P41.png
366 — R 12%, L 51%, P 37%   →  Arquivo: ppf_366_R12_L51_P37.png
367 — R 8%, L 55%, P 37%   →  Arquivo: ppf_367_R8_L55_P37.png
```

### Lote 21 de 49: triângulo 37 (IDs 371–377)

```
Lote 21/49: triângulo 37. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

371 — R 62%, L 5%, P 33%   →  Arquivo: ppf_371_R62_L5_P33.png
372 — R 67%, L 2%, P 31%   →  Arquivo: ppf_372_R67_L2_P31.png
373 — R 60%, L 10%, P 31%   →  Arquivo: ppf_373_R60_L10_P31.png
374 — R 60%, L 2%, P 38%   →  Arquivo: ppf_374_R60_L2_P38.png
375 — R 63%, L 6%, P 30%   →  Arquivo: ppf_375_R63_L6_P30.png
376 — R 59%, L 6%, P 35%   →  Arquivo: ppf_376_R59_L6_P35.png
377 — R 63%, L 2%, P 35%   →  Arquivo: ppf_377_R63_L2_P35.png
```

### Lote 22 de 49: triângulo 41 (IDs 411–417)

```
Lote 22/49: triângulo 41. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

411 — R 5%, L 62%, P 33%   →  Arquivo: ppf_411_R5_L62_P33.png
412 — R 10%, L 60%, P 31%   →  Arquivo: ppf_412_R10_L60_P31.png
413 — R 2%, L 67%, P 31%   →  Arquivo: ppf_413_R2_L67_P31.png
414 — R 2%, L 60%, P 38%   →  Arquivo: ppf_414_R2_L60_P38.png
415 — R 6%, L 63%, P 30%   →  Arquivo: ppf_415_R6_L63_P30.png
416 — R 2%, L 63%, P 35%   →  Arquivo: ppf_416_R2_L63_P35.png
417 — R 6%, L 59%, P 35%   →  Arquivo: ppf_417_R6_L59_P35.png
```

### Lote 23 de 49: triângulo 42 (IDs 421–427)

```
Lote 23/49: triângulo 42. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

421 — R 48%, L 19%, P 33%   →  Arquivo: ppf_421_R48_L19_P33.png
422 — R 52%, L 17%, P 31%   →  Arquivo: ppf_422_R52_L17_P31.png
423 — R 45%, L 24%, P 31%   →  Arquivo: ppf_423_R45_L24_P31.png
424 — R 45%, L 17%, P 38%   →  Arquivo: ppf_424_R45_L17_P38.png
425 — R 49%, L 20%, P 30%   →  Arquivo: ppf_425_R49_L20_P30.png
426 — R 45%, L 20%, P 35%   →  Arquivo: ppf_426_R45_L20_P35.png
427 — R 49%, L 16%, P 35%   →  Arquivo: ppf_427_R49_L16_P35.png
```

### Lote 24 de 49: triângulo 43 (IDs 431–437)

```
Lote 24/49: triângulo 43. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

431 — R 19%, L 48%, P 33%   →  Arquivo: ppf_431_R19_L48_P33.png
432 — R 24%, L 45%, P 31%   →  Arquivo: ppf_432_R24_L45_P31.png
433 — R 17%, L 52%, P 31%   →  Arquivo: ppf_433_R17_L52_P31.png
434 — R 17%, L 45%, P 38%   →  Arquivo: ppf_434_R17_L45_P38.png
435 — R 20%, L 49%, P 30%   →  Arquivo: ppf_435_R20_L49_P30.png
436 — R 16%, L 49%, P 35%   →  Arquivo: ppf_436_R16_L49_P35.png
437 — R 20%, L 45%, P 35%   →  Arquivo: ppf_437_R20_L45_P35.png
```

### Lote 25 de 49: triângulo 44 (IDs 441–447)

```
Lote 25/49: triângulo 44. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

441 — R 33%, L 33%, P 33%   →  Arquivo: ppf_441_R33_L33_P33.png
442 — R 38%, L 31%, P 31%   →  Arquivo: ppf_442_R38_L31_P31.png
443 — R 31%, L 38%, P 31%   →  Arquivo: ppf_443_R31_L38_P31.png
444 — R 31%, L 31%, P 38%   →  Arquivo: ppf_444_R31_L31_P38.png
445 — R 35%, L 35%, P 30%   →  Arquivo: ppf_445_R35_L35_P30.png
446 — R 30%, L 35%, P 35%   →  Arquivo: ppf_446_R30_L35_P35.png
447 — R 35%, L 30%, P 35%   →  Arquivo: ppf_447_R35_L30_P35.png
```

### Lote 26 de 49: triângulo 45 (IDs 451–457)

```
Lote 26/49: triângulo 45. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

451 — R 38%, L 38%, P 24%   →  Arquivo: ppf_451_R38_L38_P24.png
452 — R 33%, L 40%, P 26%   →  Arquivo: ppf_452_R33_L40_P26.png
453 — R 40%, L 33%, P 26%   →  Arquivo: ppf_453_R40_L33_P26.png
454 — R 40%, L 40%, P 19%   →  Arquivo: ppf_454_R40_L40_P19.png
455 — R 37%, L 37%, P 27%   →  Arquivo: ppf_455_R37_L37_P27.png
456 — R 41%, L 37%, P 22%   →  Arquivo: ppf_456_R41_L37_P22.png
457 — R 37%, L 41%, P 22%   →  Arquivo: ppf_457_R37_L41_P22.png
```

### Lote 27 de 49: triângulo 46 (IDs 461–467)

```
Lote 27/49: triângulo 46. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

461 — R 67%, L 10%, P 24%   →  Arquivo: ppf_461_R67_L10_P24.png
462 — R 62%, L 12%, P 26%   →  Arquivo: ppf_462_R62_L12_P26.png
463 — R 69%, L 5%, P 26%   →  Arquivo: ppf_463_R69_L5_P26.png
464 — R 69%, L 12%, P 19%   →  Arquivo: ppf_464_R69_L12_P19.png
465 — R 65%, L 8%, P 27%   →  Arquivo: ppf_465_R65_L8_P27.png
466 — R 70%, L 8%, P 22%   →  Arquivo: ppf_466_R70_L8_P22.png
467 — R 65%, L 12%, P 22%   →  Arquivo: ppf_467_R65_L12_P22.png
```

### Lote 28 de 49: triângulo 47 (IDs 471–477)

```
Lote 28/49: triângulo 47. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

471 — R 52%, L 24%, P 24%   →  Arquivo: ppf_471_R52_L24_P24.png
472 — R 48%, L 26%, P 26%   →  Arquivo: ppf_472_R48_L26_P26.png
473 — R 55%, L 19%, P 26%   →  Arquivo: ppf_473_R55_L19_P26.png
474 — R 55%, L 26%, P 19%   →  Arquivo: ppf_474_R55_L26_P19.png
475 — R 51%, L 22%, P 27%   →  Arquivo: ppf_475_R51_L22_P27.png
476 — R 55%, L 22%, P 22%   →  Arquivo: ppf_476_R55_L22_P22.png
477 — R 51%, L 27%, P 22%   →  Arquivo: ppf_477_R51_L27_P22.png
```

### Lote 29 de 49: triângulo 51 (IDs 511–517)

```
Lote 29/49: triângulo 51. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

511 — R 24%, L 52%, P 24%   →  Arquivo: ppf_511_R24_L52_P24.png
512 — R 19%, L 55%, P 26%   →  Arquivo: ppf_512_R19_L55_P26.png
513 — R 26%, L 48%, P 26%   →  Arquivo: ppf_513_R26_L48_P26.png
514 — R 26%, L 55%, P 19%   →  Arquivo: ppf_514_R26_L55_P19.png
515 — R 22%, L 51%, P 27%   →  Arquivo: ppf_515_R22_L51_P27.png
516 — R 27%, L 51%, P 22%   →  Arquivo: ppf_516_R27_L51_P22.png
517 — R 22%, L 55%, P 22%   →  Arquivo: ppf_517_R22_L55_P22.png
```

### Lote 30 de 49: triângulo 52 (IDs 521–527)

```
Lote 30/49: triângulo 52. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

521 — R 10%, L 67%, P 24%   →  Arquivo: ppf_521_R10_L67_P24.png
522 — R 5%, L 69%, P 26%   →  Arquivo: ppf_522_R5_L69_P26.png
523 — R 12%, L 62%, P 26%   →  Arquivo: ppf_523_R12_L62_P26.png
524 — R 12%, L 69%, P 19%   →  Arquivo: ppf_524_R12_L69_P19.png
525 — R 8%, L 65%, P 27%   →  Arquivo: ppf_525_R8_L65_P27.png
526 — R 12%, L 65%, P 22%   →  Arquivo: ppf_526_R12_L65_P22.png
527 — R 8%, L 70%, P 22%   →  Arquivo: ppf_527_R8_L70_P22.png
```

### Lote 31 de 49: triângulo 53 (IDs 531–537)

```
Lote 31/49: triângulo 53. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

531 — R 62%, L 19%, P 19%   →  Arquivo: ppf_531_R62_L19_P19.png
532 — R 67%, L 17%, P 17%   →  Arquivo: ppf_532_R67_L17_P17.png
533 — R 60%, L 24%, P 17%   →  Arquivo: ppf_533_R60_L24_P17.png
534 — R 60%, L 17%, P 24%   →  Arquivo: ppf_534_R60_L17_P24.png
535 — R 63%, L 20%, P 16%   →  Arquivo: ppf_535_R63_L20_P16.png
536 — R 59%, L 20%, P 20%   →  Arquivo: ppf_536_R59_L20_P20.png
537 — R 63%, L 16%, P 20%   →  Arquivo: ppf_537_R63_L16_P20.png
```

### Lote 32 de 49: triângulo 54 (IDs 541–547)

```
Lote 32/49: triângulo 54. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

541 — R 19%, L 62%, P 19%   →  Arquivo: ppf_541_R19_L62_P19.png
542 — R 24%, L 60%, P 17%   →  Arquivo: ppf_542_R24_L60_P17.png
543 — R 17%, L 67%, P 17%   →  Arquivo: ppf_543_R17_L67_P17.png
544 — R 17%, L 60%, P 24%   →  Arquivo: ppf_544_R17_L60_P24.png
545 — R 20%, L 63%, P 16%   →  Arquivo: ppf_545_R20_L63_P16.png
546 — R 16%, L 63%, P 20%   →  Arquivo: ppf_546_R16_L63_P20.png
547 — R 20%, L 59%, P 20%   →  Arquivo: ppf_547_R20_L59_P20.png
```

### Lote 33 de 49: triângulo 55 (IDs 551–557)

```
Lote 33/49: triângulo 55. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

551 — R 76%, L 5%, P 19%   →  Arquivo: ppf_551_R76_L5_P19.png
552 — R 81%, L 2%, P 17%   →  Arquivo: ppf_552_R81_L2_P17.png
553 — R 74%, L 10%, P 17%   →  Arquivo: ppf_553_R74_L10_P17.png
554 — R 74%, L 2%, P 24%   →  Arquivo: ppf_554_R74_L2_P24.png
555 — R 78%, L 6%, P 16%   →  Arquivo: ppf_555_R78_L6_P16.png
556 — R 73%, L 6%, P 20%   →  Arquivo: ppf_556_R73_L6_P20.png
557 — R 78%, L 2%, P 20%   →  Arquivo: ppf_557_R78_L2_P20.png
```

### Lote 34 de 49: triângulo 56 (IDs 561–567)

```
Lote 34/49: triângulo 56. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

561 — R 48%, L 33%, P 19%   →  Arquivo: ppf_561_R48_L33_P19.png
562 — R 52%, L 31%, P 17%   →  Arquivo: ppf_562_R52_L31_P17.png
563 — R 45%, L 38%, P 17%   →  Arquivo: ppf_563_R45_L38_P17.png
564 — R 45%, L 31%, P 24%   →  Arquivo: ppf_564_R45_L31_P24.png
565 — R 49%, L 35%, P 16%   →  Arquivo: ppf_565_R49_L35_P16.png
566 — R 45%, L 35%, P 20%   →  Arquivo: ppf_566_R45_L35_P20.png
567 — R 49%, L 30%, P 20%   →  Arquivo: ppf_567_R49_L30_P20.png
```

### Lote 35 de 49: triângulo 57 (IDs 571–577)

```
Lote 35/49: triângulo 57. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

571 — R 33%, L 48%, P 19%   →  Arquivo: ppf_571_R33_L48_P19.png
572 — R 38%, L 45%, P 17%   →  Arquivo: ppf_572_R38_L45_P17.png
573 — R 31%, L 52%, P 17%   →  Arquivo: ppf_573_R31_L52_P17.png
574 — R 31%, L 45%, P 24%   →  Arquivo: ppf_574_R31_L45_P24.png
575 — R 35%, L 49%, P 16%   →  Arquivo: ppf_575_R35_L49_P16.png
576 — R 30%, L 49%, P 20%   →  Arquivo: ppf_576_R30_L49_P20.png
577 — R 35%, L 45%, P 20%   →  Arquivo: ppf_577_R35_L45_P20.png
```

### Lote 36 de 49: triângulo 61 (IDs 611–617)

```
Lote 36/49: triângulo 61. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

611 — R 5%, L 76%, P 19%   →  Arquivo: ppf_611_R5_L76_P19.png
612 — R 10%, L 74%, P 17%   →  Arquivo: ppf_612_R10_L74_P17.png
613 — R 2%, L 81%, P 17%   →  Arquivo: ppf_613_R2_L81_P17.png
614 — R 2%, L 74%, P 24%   →  Arquivo: ppf_614_R2_L74_P24.png
615 — R 6%, L 78%, P 16%   →  Arquivo: ppf_615_R6_L78_P16.png
616 — R 2%, L 78%, P 20%   →  Arquivo: ppf_616_R2_L78_P20.png
617 — R 6%, L 73%, P 20%   →  Arquivo: ppf_617_R6_L73_P20.png
```

### Lote 37 de 49: triângulo 62 (IDs 621–627)

```
Lote 37/49: triângulo 62. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

621 — R 81%, L 10%, P 10%   →  Arquivo: ppf_621_R81_L10_P10.png
622 — R 76%, L 12%, P 12%   →  Arquivo: ppf_622_R76_L12_P12.png
623 — R 83%, L 5%, P 12%   →  Arquivo: ppf_623_R83_L5_P12.png
624 — R 83%, L 12%, P 5%   →  Arquivo: ppf_624_R83_L12_P5.png
625 — R 80%, L 8%, P 12%   →  Arquivo: ppf_625_R80_L8_P12.png
626 — R 84%, L 8%, P 8%   →  Arquivo: ppf_626_R84_L8_P8.png
627 — R 80%, L 12%, P 8%   →  Arquivo: ppf_627_R80_L12_P8.png
```

### Lote 38 de 49: triângulo 63 (IDs 631–637)

```
Lote 38/49: triângulo 63. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

631 — R 52%, L 38%, P 10%   →  Arquivo: ppf_631_R52_L38_P10.png
632 — R 48%, L 40%, P 12%   →  Arquivo: ppf_632_R48_L40_P12.png
633 — R 55%, L 33%, P 12%   →  Arquivo: ppf_633_R55_L33_P12.png
634 — R 55%, L 40%, P 5%   →  Arquivo: ppf_634_R55_L40_P5.png
635 — R 51%, L 37%, P 12%   →  Arquivo: ppf_635_R51_L37_P12.png
636 — R 55%, L 37%, P 8%   →  Arquivo: ppf_636_R55_L37_P8.png
637 — R 51%, L 41%, P 8%   →  Arquivo: ppf_637_R51_L41_P8.png
```

### Lote 39 de 49: triângulo 64 (IDs 641–647)

```
Lote 39/49: triângulo 64. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

641 — R 38%, L 52%, P 10%   →  Arquivo: ppf_641_R38_L52_P10.png
642 — R 33%, L 55%, P 12%   →  Arquivo: ppf_642_R33_L55_P12.png
643 — R 40%, L 48%, P 12%   →  Arquivo: ppf_643_R40_L48_P12.png
644 — R 40%, L 55%, P 5%   →  Arquivo: ppf_644_R40_L55_P5.png
645 — R 37%, L 51%, P 12%   →  Arquivo: ppf_645_R37_L51_P12.png
646 — R 41%, L 51%, P 8%   →  Arquivo: ppf_646_R41_L51_P8.png
647 — R 37%, L 55%, P 8%   →  Arquivo: ppf_647_R37_L55_P8.png
```

### Lote 40 de 49: triângulo 65 (IDs 651–657)

```
Lote 40/49: triângulo 65. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

651 — R 10%, L 81%, P 10%   →  Arquivo: ppf_651_R10_L81_P10.png
652 — R 5%, L 83%, P 12%   →  Arquivo: ppf_652_R5_L83_P12.png
653 — R 12%, L 76%, P 12%   →  Arquivo: ppf_653_R12_L76_P12.png
654 — R 12%, L 83%, P 5%   →  Arquivo: ppf_654_R12_L83_P5.png
655 — R 8%, L 80%, P 12%   →  Arquivo: ppf_655_R8_L80_P12.png
656 — R 12%, L 80%, P 8%   →  Arquivo: ppf_656_R12_L80_P8.png
657 — R 8%, L 84%, P 8%   →  Arquivo: ppf_657_R8_L84_P8.png
```

### Lote 41 de 49: triângulo 66 (IDs 661–667)

```
Lote 41/49: triângulo 66. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

661 — R 67%, L 24%, P 10%   →  Arquivo: ppf_661_R67_L24_P10.png
662 — R 62%, L 26%, P 12%   →  Arquivo: ppf_662_R62_L26_P12.png
663 — R 69%, L 19%, P 12%   →  Arquivo: ppf_663_R69_L19_P12.png
664 — R 69%, L 26%, P 5%   →  Arquivo: ppf_664_R69_L26_P5.png
665 — R 65%, L 22%, P 12%   →  Arquivo: ppf_665_R65_L22_P12.png
666 — R 70%, L 22%, P 8%   →  Arquivo: ppf_666_R70_L22_P8.png
667 — R 65%, L 27%, P 8%   →  Arquivo: ppf_667_R65_L27_P8.png
```

### Lote 42 de 49: triângulo 67 (IDs 671–677)

```
Lote 42/49: triângulo 67. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

671 — R 24%, L 67%, P 10%   →  Arquivo: ppf_671_R24_L67_P10.png
672 — R 19%, L 69%, P 12%   →  Arquivo: ppf_672_R19_L69_P12.png
673 — R 26%, L 62%, P 12%   →  Arquivo: ppf_673_R26_L62_P12.png
674 — R 26%, L 69%, P 5%   →  Arquivo: ppf_674_R26_L69_P5.png
675 — R 22%, L 65%, P 12%   →  Arquivo: ppf_675_R22_L65_P12.png
676 — R 27%, L 65%, P 8%   →  Arquivo: ppf_676_R27_L65_P8.png
677 — R 22%, L 70%, P 8%   →  Arquivo: ppf_677_R22_L70_P8.png
```

### Lote 43 de 49: triângulo 71 (IDs 711–717)

```
Lote 43/49: triângulo 71. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

711 — R 76%, L 19%, P 5%   →  Arquivo: ppf_711_R76_L19_P5.png
712 — R 81%, L 17%, P 2%   →  Arquivo: ppf_712_R81_L17_P2.png
713 — R 74%, L 24%, P 2%   →  Arquivo: ppf_713_R74_L24_P2.png
714 — R 74%, L 17%, P 10%   →  Arquivo: ppf_714_R74_L17_P10.png
715 — R 78%, L 20%, P 2%   →  Arquivo: ppf_715_R78_L20_P2.png
716 — R 73%, L 20%, P 6%   →  Arquivo: ppf_716_R73_L20_P6.png
717 — R 78%, L 16%, P 6%   →  Arquivo: ppf_717_R78_L16_P6.png
```

### Lote 44 de 49: triângulo 72 (IDs 721–727)

```
Lote 44/49: triângulo 72. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

721 — R 62%, L 33%, P 5%   →  Arquivo: ppf_721_R62_L33_P5.png
722 — R 67%, L 31%, P 2%   →  Arquivo: ppf_722_R67_L31_P2.png
723 — R 60%, L 38%, P 2%   →  Arquivo: ppf_723_R60_L38_P2.png
724 — R 60%, L 31%, P 10%   →  Arquivo: ppf_724_R60_L31_P10.png
725 — R 63%, L 35%, P 2%   →  Arquivo: ppf_725_R63_L35_P2.png
726 — R 59%, L 35%, P 6%   →  Arquivo: ppf_726_R59_L35_P6.png
727 — R 63%, L 30%, P 6%   →  Arquivo: ppf_727_R63_L30_P6.png
```

### Lote 45 de 49: triângulo 73 (IDs 731–737)

```
Lote 45/49: triângulo 73. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

731 — R 33%, L 62%, P 5%   →  Arquivo: ppf_731_R33_L62_P5.png
732 — R 38%, L 60%, P 2%   →  Arquivo: ppf_732_R38_L60_P2.png
733 — R 31%, L 67%, P 2%   →  Arquivo: ppf_733_R31_L67_P2.png
734 — R 31%, L 60%, P 10%   →  Arquivo: ppf_734_R31_L60_P10.png
735 — R 35%, L 63%, P 2%   →  Arquivo: ppf_735_R35_L63_P2.png
736 — R 30%, L 63%, P 6%   →  Arquivo: ppf_736_R30_L63_P6.png
737 — R 35%, L 59%, P 6%   →  Arquivo: ppf_737_R35_L59_P6.png
```

### Lote 46 de 49: triângulo 74 (IDs 741–747)

```
Lote 46/49: triângulo 74. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

741 — R 19%, L 76%, P 5%   →  Arquivo: ppf_741_R19_L76_P5.png
742 — R 24%, L 74%, P 2%   →  Arquivo: ppf_742_R24_L74_P2.png
743 — R 17%, L 81%, P 2%   →  Arquivo: ppf_743_R17_L81_P2.png
744 — R 17%, L 74%, P 10%   →  Arquivo: ppf_744_R17_L74_P10.png
745 — R 20%, L 78%, P 2%   →  Arquivo: ppf_745_R20_L78_P2.png
746 — R 16%, L 78%, P 6%   →  Arquivo: ppf_746_R16_L78_P6.png
747 — R 20%, L 73%, P 6%   →  Arquivo: ppf_747_R20_L73_P6.png
```

### Lote 47 de 49: triângulo 75 (IDs 751–757)

```
Lote 47/49: triângulo 75. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

751 — R 90%, L 5%, P 5%   →  Arquivo: ppf_751_R90_L5_P5.png
752 — R 95%, L 2%, P 2%   →  Arquivo: ppf_752_R95_L2_P2.png
753 — R 88%, L 10%, P 2%   →  Arquivo: ppf_753_R88_L10_P2.png
754 — R 88%, L 2%, P 10%   →  Arquivo: ppf_754_R88_L2_P10.png
755 — R 92%, L 6%, P 2%   →  Arquivo: ppf_755_R92_L6_P2.png
756 — R 88%, L 6%, P 6%   →  Arquivo: ppf_756_R88_L6_P6.png
757 — R 92%, L 2%, P 6%   →  Arquivo: ppf_757_R92_L2_P6.png
```

### Lote 48 de 49: triângulo 76 (IDs 761–767)

```
Lote 48/49: triângulo 76. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

761 — R 48%, L 48%, P 5%   →  Arquivo: ppf_761_R48_L48_P5.png
762 — R 52%, L 45%, P 2%   →  Arquivo: ppf_762_R52_L45_P2.png
763 — R 45%, L 52%, P 2%   →  Arquivo: ppf_763_R45_L52_P2.png
764 — R 45%, L 45%, P 10%   →  Arquivo: ppf_764_R45_L45_P10.png
765 — R 49%, L 49%, P 2%   →  Arquivo: ppf_765_R49_L49_P2.png
766 — R 45%, L 49%, P 6%   →  Arquivo: ppf_766_R45_L49_P6.png
767 — R 49%, L 45%, P 6%   →  Arquivo: ppf_767_R49_L45_P6.png
```

### Lote 49 de 49: triângulo 77 (IDs 771–777)

```
Lote 49/49: triângulo 77. Uma imagem por resposta, na ordem; espere eu dizer "próxima".

771 — R 5%, L 90%, P 5%   →  Arquivo: ppf_771_R5_L90_P5.png
772 — R 10%, L 88%, P 2%   →  Arquivo: ppf_772_R10_L88_P2.png
773 — R 2%, L 95%, P 2%   →  Arquivo: ppf_773_R2_L95_P2.png
774 — R 2%, L 88%, P 10%   →  Arquivo: ppf_774_R2_L88_P10.png
775 — R 6%, L 92%, P 2%   →  Arquivo: ppf_775_R6_L92_P2.png
776 — R 2%, L 92%, P 6%   →  Arquivo: ppf_776_R2_L92_P6.png
777 — R 6%, L 88%, P 6%   →  Arquivo: ppf_777_R6_L88_P6.png
```

---

## 5. Prompt avulso (para outros geradores)

Para Stable Diffusion, Midjourney ou outro gerador que não conversa, use o prompt de cada ID no arquivo `prompts-343.json`, ou copie direto do modo 2 do app. Nesses geradores, apague a última linha ("Ref ...") antes de gerar, para o número não aparecer na imagem.
