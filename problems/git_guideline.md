Git 與 GitHub 的基本使用流程是以本地端為主、GitHub 為同步與分享平台。在實際開發時，所有程式碼的撰寫、修改與測試都應該先在 VS Code 中完成，完成一個修改階段後，第一步應先確認目前 Git 所偵測到的專案狀態，確保哪些檔案被修改、新增或刪除都在預期之內。

git status

當確認狀態正確後，接下來需要告訴 Git 這些變更要被納入這次更新，因此會將目前資料夾中的所有變更加入暫存區。這個動作只是準備提交，尚未形成正式版本。

git add .

所有需要更新的檔案加入暫存區後，必須建立一次 commit，commit 代表專案在某一時間點的完整版本狀態，並透過簡短的訊息描述這次修改的內容，例如修正錯誤、新增功能或更新素材。

git commit -m "describe what you changed"

完成 commit 後，版本只存在於本地端，若要讓 GitHub 上的專案更新成最新狀態，需要將這個版本推送到遠端 repository。這個動作在視覺上看起來像是覆蓋 GitHub 上的檔案，但實際上 Git 仍會完整保留所有歷史版本。

git push

在後續開發過程中，只要再次修改程式碼、設定檔或素材，都不需要重新建立 repository，只需重複相同流程即可完成更新。

git status
git add .
git commit -m "update code or assets"
git push

若專案中有不再使用的檔案或資料夾，可以直接在本地端刪除，Git 會將刪除視為一種變更，只要照正常流程提交並推送，GitHub 上對應的檔案也會一併被刪除。

git status
git add .
git commit -m "remove unused files"
git push

Markdown 檔案（例如 README.md 或說明文件）與程式碼的處理方式完全相同，新增或修改後同樣需要加入追蹤、建立 commit，並推送到 GitHub。

git add README.md
git commit -m "add or update documentation"
git push

若曾直接在 GitHub 網站上修改過檔案，回到本地端繼續開發前，應先將遠端的最新版本同步回來，避免版本不一致或衝突。

git pull

在日常使用中，大多數情況只需要記住以下流程即可完成 GitHub 的基本操作。

git status
git add .
git commit -m "message"
git push

整體而言，程式碼應以 VS Code 作為主要的開發與測試環境，Git 負責版本管理，而 GitHub 則負責同步與分享，只要遵循本地修改、建立版本、推送同步的流程，就能穩定地管理專案。




