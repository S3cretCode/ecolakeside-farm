# EcoLakeside Farm Initiative (Team 4)
## "Sustainable Agriculture - Challenges, Opportunities, and Implications" Summit

A professional, interactive, single-page presentation website presenting a 240-hectare Environmental Farm Plan for **Lakeside Farm**, designed for a high-impact **5-minute summit pitch** and deployment on **Vercel**.

---

## 🌟 Key Features

1. **Interactive 240-ha Masterplan & GIS Explorer**:
   - **4K Drone Masterplan:** Enhanced photorealistic aerial view.
   - **GIS Blueprint Layer:** Original annotated team case study plan with contours, scale (1:5,000), and north arrow.
   - **Winter Wonderpark Mode:** Photorealistic seasonal transformation visual showing the drive-through holiday light park and frozen pond eco-skating trail.
   - **Interactive Zone Telemetry:** Clickable hotspot pins and SVG vector regions for:
     - 🥔 **Potato Crop (~100 ha / 41.7%)**: Upper western slope, sandy loam aeration, scab suppression at pH 6.0–6.5.
     - 🌽 **Corn Crop (~110 ha / 45.8%)**: Downslope bio-drainage shield, deep 2m root system, nitrate scavenging.
     - 💧 **Ecological Water Filtration Ponds (~5 ha / 2.1%)**: Terraced 3-stage constructed wetland in the northeast.
     - 🌲 **30m Natural Riparian Buffer Zone (~20 ha / 8.3%)**: Multi-canopy living bio-filter along the eastern lake shore.
     - 🦆 **Protected Wetland Reserve (~5 ha / 2.1%)**: Undisturbed southeast biodiversity sanctuary and flood buffer.
     - ⇄ **Contour Tillage**: Micro-furrows perpendicular to the eastern slope reducing runoff velocity by >70%.

2. **5-Minute Summit Presenter Mode**:
   - Floating HUD with countdown clock (`05:00`), start/pause/reset controls.
   - Built-in Web Audio API synthesizer chimes at 2:30 (halfway) and 1:00 (warning).
   - Step-by-step speaker cues synchronized to document sections.
   - Keyboard navigation (`[← / →]` or `[J / K]`) for hands-free live presenting.

3. **Soil & Water Health Plan (Manitoba & Lake Winnipeg Context)**:
   - Deep dive into coarse sandy loam dynamics in the Assiniboine Delta basin.
   - Multi-barrier watershed defense preventing agricultural phosphorus and nitrogen from reaching the lake.
   - Corn stover retention and winter rye cover cropping.

4. **Crop Synergies & Food/Water Security**:
   - Caloric efficiency of potatoes + grain/feed stability of corn.
   - Closed-loop stormwater catchment providing recycled drip irrigation without drawing from the lake.

5. **Off-Season Agritourism & Economic Contingency**:
   - October: 20-ha GPS Corn Maze, Pumpkin Patch & Ag-Ed field trips.
   - Winter: 3.5 km Drive-Through Christmas Light Festival & ice-skating circuit.
   - Long-Term Contingency: Agrivoltaic Solar Park (45 MW clean power + sheep grazing) + ALUS conservation easement.

6. **Nutrients for Life Canada Branding & 4R Stewardship**:
   - Full alignment with Fertilizer Canada’s 4R framework (Right Source, Right Rate, Right Time, Right Place).

7. **Academic Rigor (MLA 9th Edition Citations)**:
   - Complete, verified citations with live links and a one-click clipboard copy tool.

---

## 🚀 How to Run Locally

You can open `index.html` directly in any web browser, or launch a lightweight local server:

```bash
cd "Agriculture Summit"

# Using Python:
python3 -m http.server 3000

# Or using Node / npx:
npx serve .
```

Then visit [http://localhost:3000](http://localhost:3000) in your browser.

---

## 🌐 How to Deploy to Vercel

### Method 1: Vercel CLI (Instant)
```bash
cd "Agriculture Summit"
npm install -g vercel   # If not already installed
vercel
```
Follow the CLI prompts (accept defaults); Vercel will deploy your static site instantly and give you a live production URL.

### Method 2: GitHub Integration (Recommended)
1. Push this directory or repository to GitHub.
2. Log into [vercel.com](https://vercel.com) and click **"Add New Project"**.
3. Import your repository.
4. Set the **Root Directory** to `Agriculture Summit` (if deploying from a monorepo).
5. Click **Deploy**. Vercel will build and serve it globally on their Edge Network with custom domain support.
