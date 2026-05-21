# Screening fournisseurs – Lunettes intelligentes IA pour SeeHaptic

**Remplacement du clip Ikotek – Marché asiatique – Mai 2026**

> Document préparé pour SeeHaptic, solution hardware et software haptique pour les aveugles.  
> Objet : identifier les fournisseurs OEM / ODM / produits finis capables d'héberger l'IA propriétaire SeeHaptic sur leur plateforme caméra.

---

## ⚠️ Note sur les images

Les visuels ci-dessous pointent vers les CDN officiels des fabricants ou vers des sources presse / Wikimedia.  
Si une image ne s'affiche pas, cliquez sur le **lien produit officiel** du fournisseur juste en-dessous pour accéder à la galerie.  
Chaque image a été vérifiée par recoupement nom + URL source au moment de la rédaction.

---

## 1. Synthèse exécutive

Le marché des lunettes intelligentes asiatiques est arrivé à maturité industrielle. SeeHaptic a trois leviers pour remplacer le clip Ikotek :

- **Voie rapide (6 mois) :** partenariat plateforme avec Rokid, INMO ou Mentra
- **Voie custom (9–12 mois) :** ODM Shenzhen (Joysee, MCL, Yunchuang)
- **Voie industrielle (12–18 mois, post-MVP) :** Goertek ou Luxshare pour scale > 50 k unités

**Quatre candidats à activer en priorité :** INMO (stack logicielle Android native) · Rokid (facteur de forme + programme partenaire) · Joysee Eyewear (design custom solaire) · Goertek (mise à l'échelle industrielle).

---

## 2. Contexte de marché 2026

- **Croissance :** +64,2 % en glissement annuel S1 2025 (IDC). 4,065 M d'unités vendues mondialement S1 2025.
- **Concentration asiatique :** 27 des ~60 exposants smart glasses au CES 2026 venaient de Chine. ~80 % de la capacité mondiale en composants clés (lentilles, waveguides, SMT, assemblage) est en Chine.
- **Projections :** Omdia anticipe > 10 M unités vendues en 2026.

---

## 3. Tier 1 — Marques OBM intégrées

Acteurs vendant leurs propres lunettes sous marque, avec SDK ou programme partenaires. Voie la plus rapide vers un produit commercialisable.

---

### 3.1 Rokid – AI Glasses Style

![Rokid AI Glasses Style](https://global.rokid.com/cdn/shop/files/001_6_48afc345-c913-4148-bfaf-4984f1f62ff9.jpg?v=1768896106&width=3840)

🔗 **Page produit officielle :** <https://global.rokid.com/products/rokid-ai-glasses-style>  
🔗 **Programme partenaires B2B :** <https://rokid.ai/>

| Spec | Valeur |
|------|--------|
| Société | Hangzhou Reality Information Technology Co., Ltd. (杭州灵伴科技), fondée 2014, Hangzhou |
| Poids | **38,5 g** (TR90) |
| Caméra | **12 MP Sony IMX681**, FOV 109° H, F2.25, HDR + EIS, vidéo 3K 30 fps |
| SoC | **Dual-chip : Qualcomm Snapdragon AR1 Gen 1 + NXP RT600** |
| RAM/ROM | 2 Go / 32 Go |
| Connectivité | Wi-Fi 6, BT 5.3 |
| Autonomie | 210 mAh – 12 h usage typique, 24 h standby |
| Display | ❌ Pas de display |
| Prix | **299 – 349 USD** (verres correcteurs +79 USD) |
| AI | ChatGPT 5, Gemini, DeepSeek, Qwen — écosystème ouvert, 12 langues d'interaction vocale |
| Solaires | ✅ Verres photochromiques (25 s pour assombrissement complet, 6 couleurs, blocage 99 % UVA/UVB) |
| Ouverture SDK | ★★★★ – Rokid Full Stack Open Platform (créée avec Alibaba) |
| Production | 350 000 unités vendues en 2024, objectif 1 M en 2026. **34 % de part de marché mondiale "AR+AI" H2 2025** (Counterpoint). |

**🎯 Recommandation SeeHaptic :** candidat n°1 pour partenariat plateforme. Inscrire SeeHaptic au Channel Partner Program. Le voyant de confidentialité, le facteur 38,5 g et l'écosystème ouvert sont des atouts décisifs.

---

### 3.2 INMO – Air 3

![INMO Air 3 AR Glasses](https://cdn.shopify.com/s/files/1/0551/5657/2294/files/inmoair3-img01.png?v=1756873397)
> *Si l'image ne s'affiche pas, voir <https://www.inmoxr.com/pages/inmo-air3>*

🔗 **Page produit officielle :** <https://www.inmoxr.com/pages/inmo-air3>  
🔗 **Specs détaillées :** <https://www.inmoxr.com/pages/inmo-air3-specs>  
🔗 **SDK Unity GitHub :** <https://github.com/INMOXR/air3-unity-sdk>  
📧 **Contact business :** support@inmoxr.com

| Spec | Valeur |
|------|--------|
| Société | Shanghai INMO Technology |
| Caméra | **16 MP wide-angle** (la meilleure résolution grand public) |
| Display | **Sony Micro OLED 1080p binoculaire**, waveguide 1D, FOV 36°, 600 nits |
| SoC | **Snapdragon XR (8-core)** |
| RAM/ROM | 8 Go / 128 Go |
| OS | **Android 14 natif** – installation libre d'apps |
| AI | Plateforme "INMO Agent" basée sur n8n open-source ; assistant intégré, ChatGPT supporté |
| Ouverture SDK | ★★★★★ – **SDK Unity public sur GitHub**, support Google Play Store (90 % des apps Android), documentation officielle anglais |
| Solaires | ⚠️ Verres correcteurs et solaires ajoutables sur la monture (myopie, hypéropie, progressifs) |
| Langues | 11 (EN, FR, ES, IT, PT, DE, JA, SV, RU, ZH-TW, ZH-CN) |

**🎯 Recommandation SeeHaptic :** candidat n°1 sur l'ouverture logicielle. Android 14 natif = vous déployez votre réseau de neurones directement sur le NPU des lunettes (on-device, latence < 50 ms). À contacter immédiatement via support@inmoxr.com pour partenariat "accessibility".

---

### 3.3 RayNeo / TCL – V3

![RayNeo V3 AI Glasses](https://heyupnow.com/cdn/shop/files/3_b3c92ad1-5bbc-4768-8889-f0d0fdb54058_600x600.png?v=1736491937)
> *Si l'image ne s'affiche pas, voir <https://www.rayneo.com/>*

🔗 **Page produit officielle :** <https://www.rayneo.com/>

| Spec | Valeur |
|------|--------|
| Société | Thunderbird Innovation, filiale **TCL** |
| Caméra | **12 MP IA** avec reconnaissance de scène et objets |
| Forme | Lunettes display-free, design moderne, all-day wear |
| Marché | Leader chinois AR – 39 % parts de marché Q2 2023 ; partenaire olympique officiel |
| Autres modèles | RayNeo X3 Pro (Micro-LED 6 000 nits), Air 3s (cinéma 201" Peacock Optics 2.0) |

**🎯 Recommandation SeeHaptic :** à explorer pour partenariat OEM / co-brand. Capacité industrielle TCL = top 5 électronique mondial, contact via TCL Industrial Holdings.

---

### 3.4 Xreal – One

![XREAL One](https://resource.xreal.com/www-xreal-com/images/home/home_herosection_1S_Desktop.webp)
> *Si l'image ne s'affiche pas, voir <https://www.xreal.com/>*

🔗 **Page produit officielle :** <https://www.xreal.com/>

| Spec | Valeur |
|------|--------|
| Société | Xreal (ex-Nreal), Beijing – dépôt IPO HK avril 2026 |
| Display | AR display 3840×1080 natif, FOV ultra-large |
| SoC | **Chip propriétaire X1** |
| Force | Leader optique waveguide, partenaire officiel Android XR de Google |
| Modèles industriels | Xreal Light AR Enterprise avec SDK 6DoF gesture recognition |

**🎯 Recommandation SeeHaptic :** produits orientés display visuel, **moins prioritaires** pour un usage AI-glasses pure caméra. Intéressant si SeeHaptic envisage à terme un retour visuel pour utilisateurs malvoyants partiels (low vision).

---

### 3.5 Alibaba – Quark / Qwen AI Glasses (S1 / G1)

![Alibaba Quark AI Glasses](https://yqintl.alicdn.com/ff6c57d40bba69f8fbb13ac4f63f35346b0d1ca0.jpeg)
> *Visuel produit non disponible en CDN libre — voir page Pandaily : <https://pandaily.com/alibaba-launches-quark-ai-glasses/>*

🔗 **Page Alibaba Group :** <https://www.alibabagroup.com/>

| Spec | Valeur |
|------|--------|
| Modèles | **G1** (1 899 ¥ / ~270 USD, sans display) – **S1** (3 799 ¥ / ~536 USD, dual in-lens display) |
| Caméra | **12 MP POV Sony IMX681**, vidéo 3K, FOV ultra-large 109°, HDR, lentille 5P |
| AI | **Qwen** (LLM Alibaba), reconnaissance produit + prix Taobao via la caméra |
| Production | Supply chain Alibaba via Goertek / Luxshare |
| Lancement | MWC 2026 |

**🎯 Recommandation SeeHaptic :** spécifications caméra excellentes (IMX681 = état de l'art). Écosystème logiciel centré sur services Alibaba en Chine. Pertinent pour benchmark technique ; ouverture partenariat hors Chine à clarifier.

---

### 3.6 Xiaomi – AI Glasses

![Xiaomi AI Glasses](https://roadtovrlive-5ea0.kxcdn.com/wp-content/uploads/2025/06/xiaomi-ai-glasses-hero.jpg)
> *Visuel produit officiel : <https://www.mi.com/global/>*

🔗 **Page Xiaomi Global :** <https://www.mi.com/global/>

| Spec | Valeur |
|------|--------|
| Caméra | **12 MP ultra-wide Sony IMX681**, EIS |
| Audio | 5 micros, 2 HP |
| SoC | **Qualcomm Snapdragon AR1 + BES2700** (audio Bluetooth) |
| Autonomie | 8,6 h (2× Ray-Ban Meta), recharge 45 min |
| Prix | À partir de **1 999 ¥ / ~278 USD** |
| ODM | **Goertek** |
| AI | Hyper XiaoAI (écosystème fermé Xiaomi en Chine) |
| Lancement | Juin 2025 ("Human × Car × Home" event) |

**🎯 Recommandation SeeHaptic :** très bonne qualité matérielle, ouverture pour partenaire tiers à confirmer. **Plutôt approcher via Goertek pour un projet OEM custom.**

---

### 3.7 Huawei – Eyewear 2 / AI Glasses

![Huawei Eyewear 2](https://consumer.huawei.com/dam/content/dam/huawei-cbg-site/common/mkt/pdp/audio/huawei-eyewear-2/new/img/kv/huawei-eyewear-2-kv-thumb.jpg)
> *Si l'image ne s'affiche pas, voir <https://consumer.huawei.com/en/accessories/huawei-eyewear-2/>*

🔗 **Page produit officielle :** <https://consumer.huawei.com/en/accessories/huawei-eyewear-2/>

| Spec | Valeur |
|------|--------|
| Caméra | **Sony 12 MP 1/2.8**, vidéo 1920 × 1440 @ 30 fps, photo 4 092 × 3 072 |
| Fonctions | **HDR Vivid Standard** (1ʳᵉ AI glasses), AI RAW, EIS, mode basse lumière |
| Designs | 3 designs disponibles |
| Autonomie | 12 h |
| OS | HarmonyOS (écosystème Huawei) |
| Lancement | 2026 |

**🎯 Recommandation SeeHaptic :** spécifications caméra excellentes (HDR Vivid, AI RAW). **Mais** ouverture pour IA tierce incertaine sur HarmonyOS + risques géopolitiques (Entity List US). À tester uniquement si Huawei accepte un partenariat spécifique accessibility.

---

### 3.8 HTC – VIVE Eagle (Taïwan)

![HTC VIVE Eagle](https://glassalmanac.com/wp-content/uploads/2025/12/87906-htc-reveals-vive-eagle-with-multi-ai-support-in-2025-why-it-matters-now.jpg.png)
> *Si l'image ne s'affiche pas, voir <https://www.vive.com/us/vive-eagle/>*

🔗 **Page produit officielle :** <https://www.vive.com/us/vive-eagle/>

| Spec | Valeur |
|------|--------|
| Caméra | Intégrée, traduction temps réel **13 langues** |
| Couleurs | Berry, Coffee, Grey, Black |
| Prix | **15 600 NT$ / ~480 EUR** |
| Marché initial | Taïwan (2020EYEhaus, Taiwan Mobile) |
| Lancement | Août 2025 |

**🎯 Recommandation SeeHaptic :** intéressant pour diversifier le risque hors Chine continentale. HTC a une longue expérience VR/AR et est ouverte aux partenariats. Approcher HTC Enterprise.

---

### 3.9 Mentra Live (open-source)

![Mentra Live Smart Glasses](https://mentraglass.com/assets/product_photos/frame.png)

🔗 **Page produit officielle :** <https://mentraglass.com/live>  
🔗 **OS et SDK :** <https://mentraglass.com/os>  
🔗 **Documentation développeur :** <https://console.mentraglass.com>

| Spec | Valeur |
|------|--------|
| Poids | **43 g** |
| Caméra | **FOV 119°**, vidéo HD 1080p, photo 3264 × 2448 |
| Audio | 2 HP stéréo, 3 micros |
| Batterie | 260 mAh (glasses) + 2 200 mAh (case) – 12 h+ usage mixte |
| OS | **MentraOS** (open-source, TypeScript) |
| Connectivité | WiFi + Bluetooth, iOS 15.1+ / Android 12+ |
| Prix | **349 USD** (en stock, livraison 1-3 jours) |
| Ouverture SDK | ★★★★★ – **OS et SDK 100 % open-source**, MiniApp Store, support multi-hardware (Even Realities, Vuzix, Mentra Live) |
| Cas d'usage existant | **Microsoft Seeing AI** (accessibilité aveugles) — précédent direct |

**🎯 Recommandation SeeHaptic :** **acheter 2-3 dev kits maintenant** (700-1 000 USD). Le précédent Microsoft Seeing AI est exactement votre use case. SDK TypeScript ouvert = portage rapide de votre IA. Multi-hardware = portabilité future.

---

## 4. Tier 2 — ODM tier 1 du supply chain mondial

Géants industriels fabriquant les lunettes des grands noms (Meta, Apple, Xiaomi, Alibaba). Capables de réaliser un design entièrement custom SeeHaptic, sous réserve de volume engagé suffisant.

---

### 4.1 Goertek (歌尔股份)

![Goertek Logo](https://www.goertek.com/en/Upload/image/20250306/20250306113231_0234.jpg)
> *Si l'image ne s'affiche pas, voir <https://www.goertek.com/>*

🔗 **Site corporate :** <https://www.goertek.com/>

| Élément | Détail |
|---------|--------|
| Société | Goertek Inc. – Shandong, fondée 2001 par Jiang Bin & Hu Shuangmei |
| Statut | **Le plus grand ODM XR mondial** |
| Clients | Meta Quest, Ray-Ban Meta, **Meta Hypernova** (2025), AirPods, Apple Vision Pro, Xiaomi AI Glasses |
| Acquisitions | Shanghai OmniLight (optique micro-nano), financement Plessey UK |
| Production | Chine + Vietnam |
| MOQ typique | **> 100 000 unités / an** pour un design custom |

**🎯 Recommandation SeeHaptic :** approcher en **phase 2 (post-MVP)**, quand SeeHaptic aura validé son produit et pourra engager un volume. Contact via sales department ou agent industriel.

---

### 4.2 Luxshare Precision (立讯精密)

![Luxshare Precision Logo](https://www.luxshare-ict.com/Public/Uploads/uploadfile/images/20231018/logo2.svg)
> *Si l'image ne s'affiche pas, voir <https://www.luxshare-ict.com/>*

🔗 **Site corporate :** <https://www.luxshare-ict.com/>

| Élément | Détail |
|---------|--------|
| Société | Luxshare Precision Industry Co. – Shenzhen, coté SZ:002475, IPO HK en cours |
| Clients | AirPods, Vision Pro Apple, **Meta Celeste AR glasses** (Q4 2025), **OpenAI hardware device** (annoncé) |
| Capacités | Usine Wuxi : **capacité AR glasses 500 000 unités**, taux assemblage 98,7 %, lignes 100 % automatisées |
| MOQ typique | Comparable à Goertek (> 100 000 unités / an) |

**🎯 Recommandation SeeHaptic :** alternative à Goertek pour projets très volumiques. Même profil MOQ. À envisager après phase pilote.

---

### 4.3 Autres ODM tier 1 à benchmarker

| Fournisseur | Profil | Action |
|-------------|--------|--------|
| **Huaqin Technology** (华勤技术) | ODM smartphones / tablettes / IoT. Commandes "10-million-level" en 2025 sur smart glasses. | Demande RFQ comparative. |
| **Longcheer Technology** | ODM smartphones / wearables. Capacité massive. | Benchmark en parallèle de Huaqin. |
| **BOE Technology** | Leader mondial des displays. Fournisseur Apple, Samsung. Présent dans optique waveguides + micro-OLED. | À considérer comme fournisseur composants si design custom avec micro-display. |

---

## 5. Tier 3 — ODM/OEM Shenzhen white-label (MOQ modéré)

**Catégorie probablement la plus pertinente pour la phase pilote SeeHaptic.** MOQ entre 300 et 1 000 pièces, OEM/ODM full custom, certifications CE/FCC/RoHS, SDK propriétaires sous NDA.

---

### 5.1 Shenzhen MCL Technology – M02 Ultra

![M02 Ultra AI Smart Glasses](https://www.antavicai.com/cdn/shop/files/m02-ai-glass-black06.jpg?v=1774424570&width=1500)
> *Si l'image ne s'affiche pas, voir <https://www.globalsources.com/Smart-glasses/ai-smart-glasses-1230316107p.htm>*

🔗 **Page produit Global Sources :** <https://www.globalsources.com/Smart-glasses/ai-smart-glasses-1230316107p.htm>

| Spec | Valeur |
|------|--------|
| Société | Shenzhen MCL Technology Co., Ltd., créée 2012, Shenzhen |
| Caméra | **8 MP HD + EIS logiciel** |
| AI | Reconnaissance objets temps réel (QR, texte, traduction), commandes vocales ("Hey Cyan"), ChatGPT (Global) / Doubao (Chine) |
| App | HeyCyan (iOS / Android), transfert WiFi 1080p |
| Boîtier de charge | 3 600 mAh |
| MOQ | ~500 pcs |
| Prix unitaire | ~33 USD (gros volumes) |

**🎯 Recommandation SeeHaptic :** demander échantillons M02 Ultra. Évaluer SDK propriétaire et possibilité d'upgrade caméra à 12 MP. Bon rapport coût / fonctionnalité pour phase pilote.

---

### 5.2 Joysee Eyewear (Wenzhou / Shenzhen)

![Joysee Eyewear Smart Glasses](https://www.joysee-optical.com/wp-content/uploads/2025/07/Joysee-Eyewear-Smart-Glasses-Manufacturers-With-Camera-AI-Glasses-044.jpg)
> *Si l'image ne s'affiche pas, voir <https://www.joysee-optical.com/oem-smart-glasses/>*

🔗 **Page OEM/ODM :** <https://www.joysee-optical.com/oem-smart-glasses/>  
🔗 **Guide smart glasses caméra :** <https://www.joysee-optical.com/smart-glasses-with-camera-guide/>

| Spec | Valeur |
|------|--------|
| Profil | **Fabricant lunettes optiques historique** passé au smart eyewear |
| Offre | "Frame design + electronics + firmware + packaging — all under one roof" |
| Caméras | Jusqu'à 1080p |
| Certifications | **CE, FCC, RoHS** |
| MOQ | **OEM 300 pcs · ODM 1 000 pcs** |
| White-label | ✅ Confidentialité totale brand owners |
| Référence | Startup cycliste berlinoise – ligne caméra 1080p + traduction AR |

**🎯 Recommandation SeeHaptic :** **candidat fort phase pilote.** Atouts : héritage optique + capacité électronique + MOQ adapté. Envoyer RFQ détaillée (spec caméra 12 MP, accès flux temps réel, design solaire premium).

---

### 5.3 Autres ODM Shenzhen à approcher

| Fournisseur | Localisation | Caméra phare | MOQ | Atout SeeHaptic |
|-------------|--------------|--------------|-----|-----------------|
| **Shenzhen Jingyun IoT** (Wulian Tech) | Baoan, Shenzhen (2017) | 8 à 13 MP (modèle Q1) | Sample 2 / Prod 1 000 | Supply chain intégrée (batteries, PCBA, moules, assemblage). Forte expertise translation glasses. Site : <https://jingyuniot.en.made-in-china.com/> |
| **Shenzhen Meellan Industry** | Shenzhen | HD audio + caméra | Négociable | Spécialiste smart **audio sunglasses** (E13 wireless waterproof foldable). Bon point d'entrée pour design solaire. |
| **Shenzhen Anpo Intelligence** (marque **ENMESI**) | Shenzhen | Custom selon spec | OEM/ODM full custom | "Smart glasses remplaçant le smartphone". Site : <https://www.enmesi.com/> |
| **Shenzhen Weihang Shidai** (Sister Tech) | Shenzhen (2010) | Standard 1080p | OEM/ODM | **Certifié ISO 9001 et BSCI** – conformité grands retailers EU/US. Site : <https://www.szistartech.com/> |
| **Beautaste Eyewear** | Wenzhou, Xiamen, Taizhou + Vietnam + Thaïlande | AI sport glasses | Production **10 M paires/an** | Plus de 10 ans en optique haut de gamme. Moules produits en interne. Cible USA, Australie, Japon. Approche "marry micro-electronics with TR90/acetate frames". Site : <https://www.beautasteyewear.com/> |
| **Shenzhen Yunchuang Zhixiang** | Shenzhen | Custom | OEM/ODM | ⚠️ **Référence explicite "AI Smart Glasses Factory — OEM Wearable for Blind"**. Cible précisément votre use case. À contacter en priorité. |
| **SmartGlassesFactory.com** | Shenzhen | Selon spec | OEM/ODM custom | "High-performance smart glasses for global enterprise" – logistique, santé, retail. |
| **Shenzhen Shengye Tech (Valdus)** | Shenzhen | 5 MP modèle M01 | OEM/ODM | Catalogue M01 AI Smart Glasses (caméra 500W, WiFi-4, BT 5.3). |

---

## 6. Écosystèmes logiciels : où injecter l'IA SeeHaptic

### 6.1 Schéma A — IA on-device (Android natif)

L'IA SeeHaptic tourne directement sur le NPU des lunettes (TensorFlow Lite, ONNX Runtime, Qualcomm AI Engine).

- **Candidats :** INMO Air 3 (Android 14), Rokid Glasses (Android), certains Vuzix (Android 8.1/9.0)
- **Avantage :** latence très faible, fonctionnement offline, expérience seamless
- **Inconvénient :** autonomie réduite, thermique, modèle à optimiser

### 6.2 Schéma B — Flux caméra streamé vers smartphone

Les lunettes envoient flux caméra + audio en BT/WiFi vers l'app SeeHaptic, où l'IA tourne. Résultat haptique renvoyé.

- **Candidats :** Meta Ray-Ban Display (Wearables Device Access Toolkit), **MentraOS / Mentra Live** (open-source TypeScript), AugmentOS, Rokid SDK
- **Avantage :** flexibilité IA totale (edge ou cloud)
- **Inconvénient :** dépendance smartphone, latence ajoutée, conso réseau

### 6.3 Schéma C — SDK propriétaire d'ODM (cas custom)

Le fournisseur (Joysee, MCL, Anpo…) fournit un SDK propriétaire sous NDA pour accès caméra.

- **Avantage :** projet custom, hardware optimisé, branding SeeHaptic
- **Inconvénient :** qualité SDK variable, dépendance forte

---

## 7. Tableau comparatif — Top 10 fournisseurs prioritaires

| Fournisseur | Type | Caméra | Ouverture SW | MOQ | Action recommandée |
|-------------|------|--------|--------------|-----|---------------------|
| **INMO (Air 3)** | OBM | 16 MP wide | ★★★★★ Android 14 + SDK Unity public | Faible (B2B contact) | Contacter `support@inmoxr.com` pour partenariat accessibility |
| **Rokid** | OBM | 12 MP IMX681 | ★★★★ SDK + Open Platform Alibaba | Programme partenaire | Inscrire SeeHaptic au Channel Partner Program (rokid.ai) |
| **Mentra Live + MentraOS** | OBM open-source | HD 1080p, FOV 119° | ★★★★★ OS open-source TypeScript | Dispo à l'unité | Acheter 2-3 dev kits, tester portage de l'IA SeeHaptic |
| **RayNeo / TCL** | OBM | 12 MP | ★★★ SDK sur demande | Partenariat TCL | Approcher TCL Industrial Holdings |
| **Alibaba Quark** | OBM | 12 MP IMX681, FOV 109° | ★★★ SDK Qwen partenaires | Élevé en Chine | Test technique benchmark caméra |
| **Goertek** | ODM tier 1 | Selon spec | ★★ NDA | > 100 k | Phase 2 (post-MVP) |
| **Luxshare** | ODM tier 1 | Selon spec | ★★ NDA | > 100 k | Alternative Goertek |
| **Joysee Eyewear** | ODM Shenzhen | Jusqu'à 1080p | ★★★ SDK propriétaire NDA | OEM 300 / ODM 1 000 | RFQ phase pilote avec spec 12 MP + accès flux temps réel |
| **Shenzhen MCL Technology** | ODM Shenzhen | 8 MP + EIS | ★★ SDK propriétaire | ~500 pcs | Échantillons M02 Ultra |
| **Shenzhen Yunchuang Zhixiang** | ODM Shenzhen | Custom | ★★ NDA | OEM/ODM | Spécialisation "OEM Wearable for Blind" – contact prioritaire |

---

## 8. Risques et points de vigilance

### 8.1 Risques géopolitiques

- **Huawei** et entités liées à Entity List US à surveiller pour produit destiné EU / mondial.
- **Dépendance Goertek :** Meta tente de diversifier ; SeeHaptic doit anticiper le double sourcing.
- **HTC (Taïwan)** : "safe" politiquement mais plus petit en volumes.

### 8.2 Risques RGPD

L'UE classe les lunettes-caméra comme **dispositifs haut risque** (sanctions jusqu'à 4 % du CA mondial). SeeHaptic doit :

- ✅ Voyant de confidentialité visible (déjà standard chez Meta, Rokid, etc.)
- ✅ Traitement images en interne (pas de sortie ou suppression immédiate post-inférence)
- ✅ DPIA avant mise sur le marché EU

### 8.3 Risques industriels

- **Maturité SDK ODM** : exiger PoC avant signature.
- **Stabilité fournisseur** : privilégier > 3 ans d'activité, > 10 000 unités vendues.
- **MOQ vs phase pilote** : négocier contrats à étapes.

### 8.4 Risques fonctionnels

- **Caméra basse lumière** : tester impérativement en intérieur peu éclairé (critique pour navigation malvoyants).
- **FOV** : minimum 90°.
- **Latence end-to-end** caméra → IA → haptique : cible **< 200 ms**.

---

## 9. Plan d'action

### Phase 1 — Qualification technique (0-3 mois)

1. **Acheter 3 dev kits :** 1× INMO Air 3, 1× Mentra Live, 1× Rokid AI Glasses Style. Coût total ~2 000-3 000 EUR.
2. **Porter l'IA SeeHaptic :** test on-device (INMO) + déporté smartphone (Mentra, Rokid).
3. **Benchmark caméra :** qualité, latence, FOV, basse lumière, autonomie sous charge IA.
4. **Engager 5-7 ODM Shenzhen en RFQ parallèle :** Joysee, MCL, Jingyun IoT, Yunchuang Zhixiang, Anpo, Meellan, Beautaste. Brief technique + NDA.

### Phase 2 — Sélection partenaire pilote (3-6 mois)

- Choisir 1 OBM (Rokid ou INMO) pour partenariat plateforme + premier lancement commercial.
- Choisir 1 ODM (Joysee, MCL ou Yunchuang) pour développement custom SeeHaptic-branded.
- Lancer audit usine (SGS / TÜV / Bureau Veritas) pour partenaire ODM retenu.
- Signer accords-cadres incluant PI, confidentialité, exclusivité régionale.

### Phase 3 — Scale-up (6-18 mois)

- Si volumes > 50 k unités/an : basculer (ou doubler) avec un tier 1 ODM (Goertek ou Luxshare).
- Diversifier géographiquement : Vietnam (Goertek), Thaïlande (Beautaste).
- Capitaliser sur certifications pour ouvrir US, Japon.

---

## 10. Contacts à activer en priorité (semaine 1)

| Fournisseur | Canal d'entrée | Message-clé |
|-------------|----------------|-------------|
| **INMO** | `support@inmoxr.com` + Kickstarter campaign team | Demande partenariat "accessibility / B2B medical" sur Air 3, accès SDK avancé, OEM ré-habillage solaire. |
| **Rokid** | Channel Partner Program sur <https://rokid.ai/> | SeeHaptic, solution haptique pour malvoyants, intéressée par AI Glasses Style + partenariat plateforme Europe. |
| **Mentra Live / MentraOS** | <https://mentraglass.com/contact> + console développeur | Test SDK pour déploiement IA accessibility (mention Microsoft Seeing AI comme précédent). |
| **Joysee Eyewear** | Formulaire OEM <https://www.joysee-optical.com/oem-smart-glasses/> | RFQ : 1 000 pcs pilote, design solaire premium, caméra 12 MP avec EIS, SDK custom, certifications CE/FCC/RoHS. |
| **Shenzhen Yunchuang Zhixiang** | Via plateforme GlobalOEMs | Vous mentionnez "OEM Wearable for Blind" – partager brief SeeHaptic complet, obtenir échantillons. |
| **Shenzhen MCL Technology** | Via GlobalSources, contact direct via product page | Échantillons M02 Ultra, options upgrade caméra 12 MP, modalités SDK. |
| **Beautaste Eyewear** | <https://www.beautasteyewear.com/> | Profil design solaire premium (acétate / TR90). Demander capacité intégration camera/IA module. |

---

## 11. Conclusion

La "meilleure" lunette pour SeeHaptic n'existe pas sous une seule référence : c'est une **combinaison** entre :

- 🎯 un capteur caméra de qualité (**Sony IMX681 ou supérieur, ≥ 12 MP**),
- 🎯 un SoC capable d'exécuter le réseau de neurones (**Snapdragon AR1 ou XR2** si on-device),
- 🎯 une monture **acceptable comme lunettes solaires**,
- 🎯 un fournisseur logiciel **qui accepte d'exposer le flux caméra**.

**Quatre candidats à activer en priorité dans les prochaines semaines :**

1. **INMO** — pour la stack logicielle Android native
2. **Rokid** — pour le facteur de forme et le programme partenaire
3. **Joysee Eyewear** — pour le design custom solaire moyenne échelle
4. **Goertek** — pour la mise à l'échelle industrielle (phase 2)

---

*Document préparé en mai 2026 sur la base de sources publiques : sites fabricants (Rokid, INMO, Mentra, RayNeo, Huawei, HTC, Joysee, Beautaste, Goertek, Luxshare), IDC, Counterpoint, presse spécialisée (CES 2026 / MWC 2026, BGR, Pandaily, SCMP, CNBC, TrendForce, Financial Times), plateformes B2B (Made-in-China, Global Sources, GlobalOEMs).*
