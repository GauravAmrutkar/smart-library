import { Paper, Typography } from "@mui/material";

const BooksPage = () => {
  return (
    <Paper
      sx={{
        p: 4,
        m: 4,
      }}
    >
      <Typography variant="h3">
        Books
      </Typography>

      <Typography sx={{ mt: 2 }}>
        Books module will be implemented in Phase 3.
      </Typography>
    </Paper>
  );
};

export default BooksPage;