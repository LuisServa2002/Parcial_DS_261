const apiBase = "http://localhost:8000";

function setStatus(message, success = true) {
  const statusElement = document.getElementById("status-message");
  if (!statusElement) return;
  statusElement.textContent = message;
  statusElement.style.background = success ? "#d1fae5" : "#fee2e2";
  statusElement.style.color = success ? "#0f5132" : "#991b1b";
  statusElement.style.borderColor = success ? "#86efac" : "#fca5a5";
}

async function fetchIncidents() {
  const response = await fetch(`${apiBase}/`);
  const incidents = await response.json();
  const list = document.getElementById("incidents-list");

  if (!Array.isArray(incidents) || incidents.length === 0) {
    list.innerHTML = `<div class="incident-card"><p>No hay incidencias registradas aún.</p></div>`;
    return;
  }

  list.innerHTML = incidents
    .map(
      (incident) => `
      <article class="incident-card">
        <h3>${incident.title}</h3>
        <div class="incident-meta">
          <span>${incident.category}</span>
          <span>${incident.location}</span>
          <span>${incident.status}</span>
        </div>
        <p>${incident.description}</p>
        <p><strong>Reportado por:</strong> ${incident.reporter_name}</p>
        <p><strong>Fecha:</strong> ${new Date(incident.created_at).toLocaleString()}</p>
        ${incident.media_urls
          .map((url) => `<a href="${apiBase}${url}" target="_blank">Ver media</a>`)
          .join(" ")}
      </article>
    `
    )
    .join("\n");
}

async function uploadMedia(file) {
  if (!file) return [];
  const formData = new FormData();
  formData.append("file", file);
  const response = await fetch(`${apiBase}/media/upload`, {
    method: "POST",
    body: formData,
  });
  const result = await response.json();
  return [result.url];
}

async function handleSubmit(event) {
  event.preventDefault();
  const title = document.getElementById("title").value;
  const description = document.getElementById("description").value;
  const category = "Bache";
  const location = document.getElementById("location").value;
  const reporter_name = document.getElementById("reporter_name").value;
  const media_file = document.getElementById("media_file").files[0];

  const media_urls = await uploadMedia(media_file);

  try {
    setStatus("Enviando incidencia...", true);
    const response = await fetch(`${apiBase}/incidents`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        title,
        description,
        category,
        location,
        reporter_name,
        media_urls,
      }),
    });

    if (response.ok) {
      document.getElementById("incident-form").reset();
      setStatus("Incidencia creada con éxito.", true);
      await fetchIncidents();
    } else {
      const error = await response.json();
      setStatus(error.detail || "Error al crear incidencia.", false);
    }
  } catch (error) {
    setStatus("No se pudo conectar con el servidor. Verifica que el backend esté activo.", false);
  }
}

document.getElementById("incident-form").addEventListener("submit", handleSubmit);
window.addEventListener("load", () => {
  setStatus("Cargando incidencias...", true);
  fetchIncidents().then(() => setStatus("Incidencias cargadas.", true));
});
