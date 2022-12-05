library(data.table)
library(tidyverse)
df = read.delim2(file = "day05/day05-matrix.txt", sep = " ", fill = T)
orig_colnames = colnames(df)
setDT(df)
instructions <- read.delim2(file = "day05/day05-instructions.txt", sep = " ",
                            col.names = c("move", "quantity", "from", "from_instr", "to", "to_instr"))
df_orig <- df
for (i in seq_len(nrow(instructions))){
  print(i)
  if (quantity == 0){
    quantity <- instructions$quantity[i]
  }
  while (quantity > 0){
    col_to_move <- paste0("X", instructions$from_instr[i])
    row_to_move <- which(nzchar(t(df[, ..col_to_move])))[1] # data table notation, dont ask why I need the two dots...: https://stackoverflow.com/questions/41051890/r-data-table-1-10-0-why-does-a-named-column-index-value-not-work-while-a-int
    letter_to_move <- df[,..col_to_move][row_to_move,]
    col_to_put <- paste0("X", instructions$to_instr[i])
    existing_cols <- df[,!..col_to_put]
    ind_to_put = which(nzchar(t(df[,..col_to_put])))[1]-1
    if (is.na(ind_to_put)){
      ind_to_put <- nrow(df)
    }
    if (ind_to_put > 0){
      df[ind_to_put,col_to_put] = letter_to_move
      df[row_to_move, col_to_move] <- ""
    }else if (ind_to_put == 0){
      new_col = rbind(letter_to_move, df[,..col_to_put], use.names = F)
      colnames(new_col) <- col_to_put
      # if we have to add a row on top
      na_row <- t(c(rep("", ncol(existing_cols))))
      colnames(na_row) <- colnames(existing_cols)
      existing_cols[row_to_move, col_to_move] <- "" # remove moved letter
      existing_cols <- rbind(na_row, existing_cols)
      df <- data.table(new_col, existing_cols)
    }
    quantity <- quantity - 1
    print(paste("moved", letter_to_move, "from", col_to_move, "to", col_to_put))
  }
}


df %>%
  select(orig_colnames)

# read it, I can't figure out how to pull the solution, lol


### PART 2:
df <- df_orig
i = 2
for (i in seq_len(nrow(instructions))){
  print(i)
  if (quantity == 0){
    quantity <- instructions$quantity[i]
  }
  if (quantity > 1){
    col_to_move <- paste0("X", instructions$from_instr[i])
    rows_to_move <- which(nzchar(t(df[, ..col_to_move])))[1:quantity]
    letters_to_move <- df[,..col_to_move][rows_to_move,]
    col_to_put <- paste0("X", instructions$to_instr[i])
    ind_to_put = which(nzchar(t(df[,..col_to_put])))[1]-1
    existing_cols <- df[,!..col_to_put]
    if (ind_to_put == 0) {
      new_col <- rbind(letters_to_move, df[,..col_to_put], use.names = F)
      colnames(new_col) <- col_to_put

      for (i in seq_len(nrow(letters_to_move))){
        empty_row <- t(c(rep("", ncol(existing_cols))))
        cnames <- colnames(existing_cols)
        existing_cols <- rbind(empty_row, existing_cols, use.names = F)
        colnames(existing_cols) <- cnames
      }
      df <- cbind(new_col, existing_cols)
    }else
      print("i give up!")

    }
  }
  while (quantity > 0){
    col_to_move <- paste0("X", instructions$from_instr[i])
    row_to_move <- which(nzchar(t(df[, ..col_to_move])))[1] # data table notation, dont ask why I need the two dots...: https://stackoverflow.com/questions/41051890/r-data-table-1-10-0-why-does-a-named-column-index-value-not-work-while-a-int
    letter_to_move <- df[,..col_to_move][row_to_move,]
    col_to_put <- paste0("X", instructions$to_instr[i])
    existing_cols <- df[,!..col_to_put]
    ind_to_put = which(nzchar(t(df[,..col_to_put])))[1]-1
    if (is.na(ind_to_put)){
      ind_to_put <- nrow(df)
    }
    if (ind_to_put > 0){
      df[ind_to_put,col_to_put] = letter_to_move
      df[row_to_move, col_to_move] <- ""
    }else if (ind_to_put == 0){
      new_col = rbind(letter_to_move, df[,..col_to_put], use.names = F)
      colnames(new_col) <- col_to_put
      # if we have to add a row on top
      na_row <- t(c(rep("", ncol(existing_cols))))
      colnames(na_row) <- colnames(existing_cols)
      existing_cols[row_to_move, col_to_move] <- "" # remove moved letter
      existing_cols <- rbind(na_row, existing_cols)
      df <- data.table(new_col, existing_cols)
    }
    quantity <- quantity - 1
    print(paste("moved", letter_to_move, "from", col_to_move, "to", col_to_put))
  }
