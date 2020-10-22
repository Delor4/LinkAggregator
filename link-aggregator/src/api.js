import Axios from "axios"


/* API ENDPOINTS */
class Api {
  constructor() {
    this.api = Axios.create({
      //baseURL: apiHost,
      headers: {
        "Accept": "application/json",
        "Content-Type": "application/json"
      }
    });
  }
   /* CARD */
  getCards = async function () {
    return await this.api.get("/api/cards");
  }
  createCard = async function (card) {
    return await this.api.post("/api/cards", card);
  }
  updateCard = async function (card) {
    return await this.api.put("/api/cards/" + card.id, card);
  }
  deleteCard = async function (id) {
    return await this.api.delete("/api/cards/" + id);
  }
  /* LINK */
  createLink = async function (link) {
    return await this.api.post("/api/links", link)
  }
  updateLink = async function (link) {
    return await this.api.put("/api/links/" + link.id, link)
  }
  deleteLink = async function (id) {
    return await this.api.delete("/api/links/" + id);
  }
  /* TAG */
  getTags = async function () {
    return await this.api.get("/api/tags");
  }
  createTag = async function (tag) {
    return await this.api.post("/api/tags", tag);
  }
  updateTag = async function (tag) {
    return await this.api.put("/api/tags/" + tag.id, tag);
  }
  deleteTag = async function (id) {
    return await this.api.delete("/api/tags/" + id);
  }
  /* CARD TAGS */
  getCardTags = async function (card_id) {
    return await this.api.get("/api/cards/" + card_id + "/tags");
  }
  createCardTag = async function (card_id, tag_id) {
    return await this.api.post("/api/cards/" + card_id + "/tags", { 'tag_id': tag_id });
  }
  deleteCardTag = async function (card_id, tag_id) {
    return await this.api.delete("/api/cards/" + card_id + "/tags/" + tag_id);
  }
}

const api = new Api()

export default api
