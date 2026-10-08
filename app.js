/**
 * EcoLakeside Farm Initiative — Presentation & Spatial Data Engine
 * Team 4 Case Study | Sustainable Agriculture Summit
 * Enhanced with 3D Perspective Tilt, Smooth Transitions, and Agronomic Telemetry
 */

const ZONE_DATA = {
  potatoes: {
    title: "Potato Production Zone",
    badge: "100 Hectares (41.7% Area)",
    color: "#f59e0b",
    colorBg: "rgba(245, 158, 11, 0.12)",
    colorBorder: "rgba(245, 158, 11, 0.4)",
    slopePosition: "Upper Slope / Western Elevation",
    soilType: "Sandy Loam, Target pH 6.0 to 6.5",
    rationale: "Located on the highest ground of the property to eliminate the hazard of waterlogging and root rot. Sandy loam provides loose, friable pore space required for unrestricted tuber expansion, uniform sizing, and clean mechanical harvesting without soil clods.",
    lakeProtection: "Contour tillage furrows run perpendicular to the eastern slope, trapping rainfall in micro-reservoirs. A winter rye cover crop is seeded immediately following early harvest to anchor sandy loam against winter wind and spring melt erosion.",
    agronomyDetails: [
      { label: "Pest Protection", value: "Garlic companion rows emit pungent sulfur volatiles that naturally mask potato scent and repel Colorado potato beetles." },
      { label: "Pollinator Allies", value: "Native bumblebees (*Bombus*) provide sonic 'buzz pollination' that vibrates blooms and strengthens fruit/seed sets." },
      { label: "Drought Precautions", value: "Loamy biochar and composted manure boost moisture holding, while precision drip irrigation delivers recycled pond water." }
    ]
  },
  garlic: {
    title: "Hardneck Garlic Companion Zone",
    badge: "110 Hectares (45.8% Area)",
    color: "#10b981",
    colorBg: "rgba(16, 185, 129, 0.12)",
    colorBorder: "rgba(16, 185, 129, 0.4)",
    slopePosition: "Mid to Lower Slope Companion Plain",
    soilType: "Sandy Loam with Organic Matter, pH 6.2 to 6.8",
    rationale: "Planting garlic alongside potatoes provides world-class biological companion benefits. Garlic releases pungent sulfur volatiles that naturally mask potato scent and repel Colorado potato beetles, aphids, and flea beetles, eliminating synthetic insecticide sprays.",
    lakeProtection: "Garlic's moderate nutrient requirements and compact root network reduce nitrogen leaching. Planting across the slope perpendicular to runoff creates living barriers that hold water and stop topsoil loss.",
    agronomyDetails: [
      { label: "Natural Insect Shield", value: "Repels Colorado potato beetles and soil pests naturally without chemical pesticides (supported by Gilmour Companion Guide)." },
      { label: "Staggered Harvest", value: "Harvested in July/August, allowing early summer cover crops (clover, buckwheat) to restore organic matter before winter." },
      { label: "High Market Value", value: "Generates $8–$14/kg farmgate revenue, providing premium economic stability alongside potato staple production." }
    ]
  },
  filtration: {
    title: "Ecological Water Filtration System",
    badge: "~5 Hectares (2.1% Area)",
    color: "#0ea5e9",
    colorBg: "rgba(14, 165, 233, 0.12)",
    colorBorder: "rgba(14, 165, 233, 0.4)",
    slopePosition: "Northeast Topographic Catchment",
    soilType: "Terraced Constructed Wetland and Settling Ponds",
    rationale: "A three-stage biological filtration complex situated at the natural drainage convergence in the northeast corner. It captures agricultural surface runoff and tile drainage before it reaches the lake.",
    lakeProtection: "Stage 1 settles suspended sands and silts. Stage 2 utilizes native bulrushes and cattails for vegetative phosphorus and nitrogen bio-absorption. Stage 3 stores polished, stabilized water for irrigation recycling.",
    agronomyDetails: [
      { label: "Phosphorus Sequestration", value: "Binds particulate and dissolved reactive phosphorus, removing triggers for blue-green algae." },
      { label: "Water Recycling", value: "Recovers spring snowmelt and summer rainfall for closed-loop crop irrigation." },
      { label: "Manitoba Standards", value: "Exceeds water protection guidelines established for the Lake Winnipeg basin." }
    ]
  },
  riparian: {
    title: "30-Meter Natural Riparian Buffer",
    badge: "~20 Hectares (8.3% Area)",
    color: "#22c55e",
    colorBg: "rgba(34, 197, 94, 0.12)",
    colorBorder: "rgba(34, 197, 94, 0.4)",
    slopePosition: "Eastern Lake Shoreline Margin",
    soilType: "Native Riparian Alluvial Forest Profile",
    rationale: "A continuous 30-meter wide non-cultivated multi-canopy buffer extending along the full eastern shoreline. Designed according to provincial riparian health standards.",
    lakeProtection: "Combines deep-rooted willows, trembling aspen, red-osier dogwood, and native prairie grasses. This living vegetative barrier traps over 85% of particulate sediment and stabilizes the shore against wave erosion.",
    agronomyDetails: [
      { label: "Sediment Trapping", value: "Dense perennial turf and shrub roots trap surface runoff and filter shallow groundwater." },
      { label: "Bank Integrity", value: "Deep root tensile strength prevents shoreline bank slumping during high spring water levels." },
      { label: "Wildlife Corridor", value: "Maintains an unbroken migratory corridor for waterfowl, bumblebee pollinators, and predatory insects." }
    ]
  },
  wetland: {
    title: "Protected Wetland Reserve",
    badge: "~5 Hectares (2.1% Area)",
    color: "#14b8a6",
    colorBg: "rgba(20, 184, 166, 0.12)",
    colorBorder: "rgba(20, 184, 166, 0.4)",
    slopePosition: "Southeast Shoreline Sanctuary",
    soilType: "Hydric Wetland Peat and Saturated Silt",
    rationale: "An undisturbed natural wetland retained in its native state, functioning as a permanent biodiversity refuge and hydrological surge buffer.",
    lakeProtection: "Absorbs seasonal storm surges and regulates groundwater recharge into the lake without thermal or chemical disturbance.",
    agronomyDetails: [
      { label: "Biodiversity Sanctuary", value: "Critical nesting habitat for native waterfowl and amphibians, maintaining ecological balance." },
      { label: "Zero Disturbance", value: "Maintained under a strict zero-chemical and zero-machinery exclusion perimeter." },
      { label: "Carbon Storage", value: "Permanent wetland biomass preserves accumulated organic carbon." }
    ]
  },
  contour: {
    title: "Perpendicular Contour Farming",
    badge: "Entire Cultivated Landscape (210 ha)",
    color: "#e2e8f0",
    colorBg: "rgba(226, 232, 240, 0.12)",
    colorBorder: "rgba(226, 232, 240, 0.4)",
    slopePosition: "Full Eastern Descending Slope",
    soilType: "Contoured Sandy Loam Micro-Terraces",
    rationale: "All field operations, planting rows, and cultivating passes are oriented along precise contour lines perpendicular to the slope descending toward the lake.",
    lakeProtection: "Every raised furrow acts as a natural mini-dam. This cuts surface water runoff velocity by over 70%, trapping water in place, preventing soil rills, and protecting valuable topsoil.",
    agronomyDetails: [
      { label: "Topsoil Protection", value: "Stops severe water and wind erosion common on sloping sandy loam fields." },
      { label: "Moisture Retention", value: "Captures rain in furrows, guarding crops against mid-summer prairie drought." },
      { label: "Fuel Efficiency", value: "Tractor passes along level elevation lines require significantly less fuel." }
    ]
  }
};

let activeZoneKey = 'potatoes';

document.addEventListener('DOMContentLoaded', () => {
  setupMapInteractions();
  setupMapModeSwitcher();
  setupPitchPresenter();
  setup3DTilt();
  setupCitationsCopy();
  setupSeasonalModal();
  setupMobileMenu();
  updateZoneInspector(activeZoneKey);
});

function setupMapInteractions() {
  const pins = document.querySelectorAll('.pin-marker');
  pins.forEach(pin => {
    pin.addEventListener('click', () => {
      const zone = pin.getAttribute('data-zone');
      selectZone(zone);
    });
  });

  const svgRegions = document.querySelectorAll('.map-svg-region');
  svgRegions.forEach(region => {
    region.addEventListener('click', () => {
      const zone = region.getAttribute('data-zone');
      selectZone(zone);
    });
  });

  const zoneNavButtons = document.querySelectorAll('.zone-nav-btn');
  zoneNavButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const zone = btn.getAttribute('data-zone');
      selectZone(zone);
    });
  });
}

function selectZone(zoneKey) {
  if (!ZONE_DATA[zoneKey]) return;
  activeZoneKey = zoneKey;

  document.querySelectorAll('.zone-nav-btn').forEach(btn => {
    if (btn.getAttribute('data-zone') === zoneKey) {
      btn.classList.add('bg-emerald-600', 'text-white', 'border-emerald-400');
      btn.classList.remove('bg-transparent', 'text-slate-300', 'border-white/10');
    } else {
      btn.classList.remove('bg-emerald-600', 'text-white', 'border-emerald-400');
      btn.classList.add('bg-transparent', 'text-slate-300', 'border-white/10');
    }
  });

  document.querySelectorAll('.map-svg-region').forEach(reg => {
    if (reg.getAttribute('data-zone') === zoneKey) {
      reg.classList.add('active-region');
    } else {
      reg.classList.remove('active-region');
    }
  });

  updateZoneInspector(zoneKey);
}

function updateZoneInspector(zoneKey) {
  const data = ZONE_DATA[zoneKey];
  const inspector = document.getElementById('zone-inspector-content');
  if (!inspector) return;

  inspector.innerHTML = `
    <div class="animate-fadeIn">
      <div class="mb-4">
        <span class="text-xs font-mono uppercase tracking-[0.2em] block mb-1 font-semibold" style="color: ${data.color}">Spatial Unit</span>
        <h3 class="text-2xl sm:text-3xl font-serif text-ivory flex items-center justify-between">
          <span>${data.title}</span>
        </h3>
        <span class="inline-block mt-1.5 px-3 py-1 rounded text-xs font-medium border" style="background: ${data.colorBg}; border-color: ${data.colorBorder}; color: ${data.color};">
          ${data.badge}
        </span>
      </div>

      <div class="grid grid-cols-2 gap-3 mb-5 text-sm sm:text-base">
        <div class="p-3.5 curator-card">
          <span class="block text-xs text-slate-400 uppercase tracking-wider mb-1 font-semibold">Topography</span>
          <span class="text-ivory font-medium">${data.slopePosition}</span>
        </div>
        <div class="p-3.5 curator-card">
          <span class="block text-xs text-slate-400 uppercase tracking-wider mb-1 font-semibold">Soil Profile</span>
          <span class="text-ivory font-medium">${data.soilType}</span>
        </div>
      </div>

      <div class="mb-5">
        <h4 class="text-xs sm:text-sm font-semibold uppercase tracking-wider mb-2 flex items-center gap-2" style="color: ${data.color}">
          <span class="w-2 h-2 rounded-full" style="background: ${data.color}"></span>
          Agronomic Defense
        </h4>
        <p class="text-sm sm:text-base text-slate-200 leading-relaxed font-normal">${data.rationale}</p>
      </div>

      <div class="mb-5 p-4 rounded-xl" style="background: rgba(2, 132, 199, 0.08); border-left: 3px solid #38bdf8;">
        <h4 class="text-xs sm:text-sm font-semibold text-sky-300 uppercase tracking-wider mb-1.5">
          Watershed Protection Function
        </h4>
        <p class="text-sm sm:text-base text-sky-100/90 leading-relaxed font-normal">${data.lakeProtection}</p>
      </div>

      <div class="space-y-2.5 pt-2 border-t border-white/10">
        <h4 class="text-xs text-slate-400 uppercase tracking-wider mb-2 font-semibold">Technical Specifications</h4>
        ${data.agronomyDetails.map(item => `
          <div class="text-sm p-3.5 rounded-lg bg-black/40 border border-white/5 transition-colors hover:border-emerald-500/30">
            <span class="text-ivory font-medium block mb-1">${item.label}</span>
            <span class="text-slate-200 font-normal leading-relaxed">${item.value}</span>
          </div>
        `).join('')}
      </div>
    </div>
  `;
}

function setupMapModeSwitcher() {
  const buttons = document.querySelectorAll('.map-mode-btn');
  const mapImage = document.getElementById('main-farm-image');
  const svgOverlay = document.getElementById('map-svg-overlay');
  const hotspotsContainer = document.getElementById('map-hotspots');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      const mode = btn.getAttribute('data-mode');

      buttons.forEach(b => {
        b.classList.remove('bg-emerald-600', 'text-white', 'font-semibold', 'shadow-md');
        b.classList.add('text-slate-400', 'bg-transparent');
      });
      btn.classList.add('bg-emerald-600', 'text-white', 'font-semibold', 'shadow-md');
      btn.classList.remove('text-slate-400', 'bg-transparent');

      if (mode === 'clean') {
        mapImage.src = 'assets/farm_aerial_clean.jpg';
        svgOverlay.style.display = 'block';
        hotspotsContainer.style.display = 'block';
      } else if (mode === 'original') {
        mapImage.src = 'assets/farm_plan_original.jpg';
        svgOverlay.style.display = 'none';
        hotspotsContainer.style.display = 'block';
      } else if (mode === 'winter') {
        mapImage.src = 'assets/winter_holiday_farm.jpg';
        svgOverlay.style.display = 'none';
        hotspotsContainer.style.display = 'none';
      }
    });
  });
}

// 3D Perspective Tilt for the Map Container
function setup3DTilt() {
  const container = document.getElementById('map-interactive-container');
  const card = document.getElementById('map-card-element');
  if (!container || !card) return;

  container.addEventListener('mousemove', (e) => {
    const rect = container.getBoundingClientRect();
    const x = e.clientX - rect.left;
    const y = e.clientY - rect.top;

    const centerX = rect.width / 2;
    const centerY = rect.height / 2;

    const rotateX = ((y - centerY) / centerY) * -4.5; // Max 4.5 deg tilt
    const rotateY = ((x - centerX) / centerX) * 4.5;

    card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.008, 1.008, 1.008)`;
  });

  container.addEventListener('mouseleave', () => {
    card.style.transform = `perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)`;
  });
}

function setupPitchPresenter() {
  const toggleBtn = document.getElementById('toggle-pitch-hud-btn');
  const hud = document.getElementById('pitch-presenter-hud');
  const prevStepBtn = document.getElementById('hud-prev-step');
  const nextStepBtn = document.getElementById('hud-next-step');

  const pitchSteps = [
    { target: '#hero', title: '1. Introduction: 240-ha Vision' },
    { target: '#overview', title: '2. Limitations & Site Challenges' },
    { target: '#masterplan', title: '3. The Plan: Potatoes & Garlic' },
    { target: '#soil-water', title: '4. Environment & Watershed Defense' },
    { target: '#alternate-uses', title: '5. Off-Season & Winter Park' },
    { target: '#recap', title: '6. Executive Recap & Takeaways' }
  ];

  let currentStepIdx = 0;

  function updateStepUI() {
    const step = pitchSteps[currentStepIdx];
    const stepNum = document.getElementById('hud-step-num');
    const stepTitle = document.getElementById('hud-step-title');
    const progressBar = document.getElementById('hud-progress-bar');

    if (stepNum) stepNum.textContent = `${currentStepIdx + 1} of ${pitchSteps.length}`;
    if (stepTitle) stepTitle.textContent = step.title;
    if (progressBar) {
      const percentage = ((currentStepIdx + 1) / pitchSteps.length) * 100;
      progressBar.style.width = `${percentage}%`;
    }

    const el = document.querySelector(step.target);
    if (el) {
      el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  }

  function openPresenter() {
    if (!hud) return;
    hud.classList.add('hud-active');
    updateStepUI();
  }

  function closePresenter() {
    if (!hud) return;
    hud.classList.remove('hud-active');
  }

  if (toggleBtn && hud) {
    toggleBtn.addEventListener('click', () => {
      if (hud.classList.contains('hud-active')) {
        closePresenter();
      } else {
        openPresenter();
      }
    });
  }

  if (nextStepBtn) {
    nextStepBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentStepIdx < pitchSteps.length - 1) {
        currentStepIdx++;
        updateStepUI();
      }
    });
  }

  if (prevStepBtn) {
    prevStepBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      if (currentStepIdx > 0) {
        currentStepIdx--;
        updateStepUI();
      }
    });
  }

  window.addEventListener('keydown', (e) => {
    if (hud && hud.classList.contains('hud-active')) {
      if (e.key === 'ArrowRight' || e.key === 'k') {
        if (currentStepIdx < pitchSteps.length - 1) {
          currentStepIdx++;
          updateStepUI();
        }
      } else if (e.key === 'ArrowLeft' || e.key === 'j') {
        if (currentStepIdx > 0) {
          currentStepIdx--;
          updateStepUI();
        }
      } else if (e.key === 'Escape') {
        closePresenter();
      }
    }
  });

  // Export helper for other triggers (like mobile menu)
  window.openPresentationMode = openPresenter;
}

function setupSeasonalModal() {
  const modal = document.getElementById('seasonal-modal');
  const openButtons = document.querySelectorAll('.open-seasonal-modal-btn');
  const closeBtn = document.getElementById('close-seasonal-modal-btn');

  if (!modal) return;

  openButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const season = btn.getAttribute('data-season') || 'winter';
      showSeasonTab(season);
      modal.classList.remove('hidden');
      modal.classList.add('flex');
    });
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    });
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      modal.classList.add('hidden');
      modal.classList.remove('flex');
    }
  });

  const modalTabs = document.querySelectorAll('.modal-season-tab');
  modalTabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.getAttribute('data-tab');
      showSeasonTab(target);
    });
  });
}

function showSeasonTab(seasonKey) {
  const tabs = document.querySelectorAll('.modal-season-tab');
  const panes = document.querySelectorAll('.season-tab-content');

  tabs.forEach(t => {
    if (t.getAttribute('data-tab') === seasonKey) {
      t.classList.add('bg-emerald-600', 'text-white', 'font-semibold');
      t.classList.remove('text-slate-400', 'bg-transparent');
    } else {
      t.classList.remove('bg-emerald-600', 'text-white', 'font-semibold');
      t.classList.add('text-slate-400', 'bg-transparent');
    }
  });

  panes.forEach(p => {
    if (p.getAttribute('id') === `season-content-${seasonKey}`) {
      p.classList.remove('hidden');
    } else {
      p.classList.add('hidden');
    }
  });
}

function setupCitationsCopy() {
  const copyBtn = document.getElementById('copy-citations-btn');
  if (!copyBtn) return;

  copyBtn.addEventListener('click', () => {
    const citationsText = `Delta Farmland: https://deltafarmland.ca/cover-crop-for-winter-how-to-protect-farm-soil/

Gilmour: https://gilmour.com/companion-planting-chart-guide/

Fertilizer Canada: https://fertilizercanada.ca/our-focus/stewardship/4rs-across-canada/

Water Security Agency (WSask): https://wsask.ca

Wakefield Biochar: https://wakefieldbiochar.com/learning-center/loamy-soil-conditions/?srsltid=AU7gw4U98rqcesSvCZQJeLGF0Z9iRW7Zg1JkJJUyJ1ManHROj-41CNsl`;

    navigator.clipboard.writeText(citationsText).then(() => {
      const originalHTML = copyBtn.innerHTML;
      copyBtn.textContent = 'Links Copied';
      copyBtn.classList.add('text-emerald-400');
      setTimeout(() => {
        copyBtn.innerHTML = originalHTML;
        copyBtn.classList.remove('text-emerald-400');
      }, 2500);
    }).catch(err => {
      console.error("Copy failed:", err);
    });
  });
}

function setupMobileMenu() {
  const openBtn = document.getElementById('mobile-menu-open-btn');
  const closeBtn = document.getElementById('mobile-menu-close-btn');
  const menu = document.getElementById('mobile-fullscreen-menu');
  const links = document.querySelectorAll('.mobile-nav-link');
  const pitchBtn = document.getElementById('mobile-menu-pitch-btn');

  if (!menu) return;

  function openMenu() {
    menu.classList.remove('menu-closed');
    menu.classList.add('menu-open');
    document.body.classList.add('overflow-hidden');
  }

  function closeMenu() {
    menu.classList.remove('menu-open');
    menu.classList.add('menu-closed');
    document.body.classList.remove('overflow-hidden');
  }

  if (openBtn) {
    openBtn.addEventListener('click', openMenu);
  }

  if (closeBtn) {
    closeBtn.addEventListener('click', closeMenu);
  }

  links.forEach(link => {
    link.addEventListener('click', () => {
      closeMenu();
    });
  });

  if (pitchBtn) {
    pitchBtn.addEventListener('click', () => {
      closeMenu();
      if (typeof window.openPresentationMode === 'function') {
        window.openPresentationMode();
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && menu.classList.contains('menu-open')) {
      closeMenu();
    }
  });
}

